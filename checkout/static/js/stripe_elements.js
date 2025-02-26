let stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
let clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': { color: '#aab7c4' }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

let card = elements.create('card', { style: style });
card.mount('#card-element');

card.addEventListener('change', function(event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class='icon' role='alert'>
                <i class='fas fa-times'></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

let form = document.getElementById('payment-form');

form.addEventListener('submit', async function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/checkout/cache_checkout_data/';

    try {
        await $.post(url, postData);

        const { paymentMethod, error } = await stripe.createPaymentMethod({
            type: "card",
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        });

        if (error) {
            throw new Error(error.message);
        }

        console.log("Client Secret:", clientSecret);
        console.log("Payment Method ID:", paymentMethod.id);

        const result = await stripe.confirmCardPayment(clientSecret, {
            payment_method: paymentMethod.id,
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            }
        });

        if (result.error) {
            let errorDiv = document.getElementById('card-errors');
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    } catch (error) {
        console.error("Error:", error);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        card.update({ 'disabled': false });
        $('#submit-button').attr('disabled', false);
    }
});
