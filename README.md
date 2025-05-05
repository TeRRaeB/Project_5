# ![logo](/doc/iamresponse.png) 
# Golden Hoof
**The project was made on the basis of the upcoming Boutique Ado project**

*You can see project (Heroku) ->> [Golden Hoof](https://golden-hoof-e080ba2678ec.herokuapp.com/).


## Project Goal

This project was created as part of my full-stack development diploma at Code Institute. The main objective was to improve and showcase my skills in web development, including both front-end and back-end technologies. 

**Golden Hoof** is a farm that produces a wide range of high-quality products, such as meat, milk, eggs, vegetables, fruits, berries, and more. The goal of this project is not only to demonstrate my technical abilities but also to build a functional and user-friendly platform for a real-world business, helping to manage and present the farm’s products online in an efficient and attractive way.

## Features

- **Product Listings:** A user-friendly interface to browse farm products.
- **Product Details:** Each product page displays detailed information, including description, price, ratings and reviews.
- **User Authentication:** Secure user login and registration for access to restricted areas.
- **Responsive Design:** The website is fully responsive and optimized for mobile and desktop views.
- **Admin Panel:** Admins can manage products, update information, contact form response, and monitor orders. 
  

## User Experience

### Target Group

The target group for the **Golden Hoof** website includes individuals and families interested in purchasing high-quality farm products such as fresh meat, dairy, eggs, vegetables, fruits, and berries. The site is aimed at health-conscious consumers looking for locally sourced, fresh produce.

### Visitors Goals

#### First-Time Visitor Goals

- **Discover the Farm's Offerings:** First-time visitors want to learn about the products offered by Golden Hoof, including the variety of items such as meat, milk, eggs, and produce.
- **Understand the Farm’s Values and Mission:** New visitors are likely interested in knowing the farm’s story, values, and how products are sourced and produced.
- **Ease of Navigation and Search:** A key goal for first-time visitors is finding an intuitive and easy-to-navigate website to help them quickly understand what the farm offers and where to purchase the products.
- **Explore the Product Details:** They will likely want to dive into specific products, looking for detailed information such as prices, descriptions.
- **Create an Account or Make a Purchase:** Some visitors may be looking to sign up, either to make a purchase or to keep track of future products and offers.

#### Returning Visitors Goals

- **Quick Access to Products of Interest:** Returning visitors are familiar with the website, so they seek a faster way to browse or find specific products they have purchased before or are interested in.
- **Place an Order or Refill a Previous Order:** Returning visitors may want to place a new order or repeat a previous purchase, often looking for a streamlined checkout process.
- **Track Orders or View Purchase History:** They might wish to track the status of their orders or view past purchases for easier reordering.

#### Frequent Visitors Goals

- **Loyalty and Rewards:** Frequent visitors might be looking for loyalty programs, rewards, or discounts as a thank-you for their ongoing business.
- **Stay Updated on New Arrivals or Promotions:** They want to be informed about the latest product arrivals, seasonal items, or special offers.
- **Engage with the Farm Community:** Frequent visitors may be looking for opportunities to interact more with the farm, such as joining newsletters, events, or social media communities.
- **Access Personalized Recommendations:** Based on their purchase history or browsing preferences, frequent visitors might appreciate personalized product recommendations or tailored promotions.

## Design

### Wireframes  
#### home part#1 

![wireframe home part#1](/doc/balsamiq-main.png)

#### home part#2 

![wireframe home part#2](/doc/balsamiq-main2.png)

**home part#3**

![wireframe home part#3](/doc/balsamiq-main3.png)

**bag**

![wireframe bag](/doc/balsamiq-bag.png)

**product detail**

![wireframe product detail](/doc/balsamiq-product-detail.png)

**profile user**

![wireframe profile user](/doc/balsamiq-profile.png) 


### GUI 

**Home page**
![GUI home page](/doc/gui-main.png) 

**Products page**
![GUI Products page](/doc/giu-products.png)
**Product detail page**
![GUI Product detail page](/doc/giu-product-detail.png)
**Bag page**
![GUI Bag page](/doc/giu-bag.png) 
**home page**
![GUI Checkout page](/doc/giu-checkout.png)



### Colors
![colors](/doc/muzli-colors.svg)
## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Backend:** Python, Django
- **Database:** Postgrest
- **Version Control:**  GitHub

## Development 
### Database
The project uses **PostgreSQL** as the database management system. The database structure is designed to ensure efficient organization of products, categories, and user interactions such as reviews and ratings.

### Database Structure

- **Categories and Subcategories:**  
  - Products are organized into **categories** and **subcategories**.  
  - A subcategory is always linked to a parent category, ensuring a structured classification of products.

- **Products:**  
  - Each product is associated with a **category** and a **subcategory**.  
  - This structure allows for easy filtering and navigation within the product catalog.

- **Reviews and Ratings:**  
  - The project includes a **Review and Rating system** to gather user feedback.  
  - Each review consists of a **text comment** and an optional **rating (1-5 stars)**.  
  - Users can also submit a **rating without a review** by selecting a star rating under the product description.  
  - A user can **only rate a product once**, either by submitting a review with a rating or just selecting a rating.  
  - Ratings from reviews and standalone ratings contribute to the product's **overall rating score**.

This database structure ensures a **well-organized product catalog**, **user-friendly navigation**, and **fair rating system** that prevents duplicate ratings while allowing users to express their opinions effectively.


#### Rating


*** You can leave a quick rating above the "add to cart" button ***

![rating #1](/doc/rating1.png)

*** The star is illuminated using JS ***


![rating #2](/doc/rating2.png)

*** If the user has given a rating, the stars will be shaded depending on the rating ***

![rating #3](/doc/rating3.png)

*** You can also give a rating when writing a review about a product. ***

![rating #4](/doc/rating4.png)


### Agile Development Methods

This project utilizes Agile Development Methods to manage development and ensure efficient delivery.
 [Kanban board](https://github.com/users/TeRRaeB/projects/3).


![Kanban board](/doc/kanban.png)

## Features

The core functionality of the **Golden Hoof** website was implemented based on the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) project, including standard e-commerce features.

### Main Features

The **Golden Hoof** website provides a seamless shopping experience for customers looking to buy high-quality farm products. The platform includes the following key features:

- **Product Catalog with Categories and Subcategories**  
  - Products are well-organized into **categories** and **subcategories** for easy navigation.  
  - Customers can browse through different product types such as meat, dairy, eggs, vegetables, fruits, and berries.  

- **Product Details Page**  
  - Each product has a dedicated page with **detailed descriptions**, **images**, and **pricing information**.  

- **User Reviews and Ratings**  
  - Customers can **rate products** and leave **detailed reviews** to share their experiences.  
  - Users can submit a **rating without a review** by selecting a star rating under the product description.  
  - A customer can **only rate a product once**, ensuring a fair rating system.  
  - The overall product rating is calculated dynamically and affects sorting when filtering by rating.  
  - The latest reviews are dynamically displayed on the homepage.  

- **User Authentication and Account Management**  
  - Secure **user registration and login** system.  
  - Logged-in users can manage their **profile**, view **order history**, and track purchases.  

- **Shopping Cart and Checkout**  
  - Users can **add products to the cart** and proceed to a **secure checkout**.  
  - The checkout process is designed to be user-friendly and efficient.  

- **Contact and Support**  
  - A **Contact Us** page allows users to send inquiries and get assistance from the farm.  
  - Customers can find farm location details and business hours.  
  - The contact form enables users to submit questions directly to the administration.  
  - Administrators have access to these messages through a dedicated **Admin Panel** button, where they can **view and delete** inquiries.  

- **Mobile-Friendly and Responsive Design**  
  - The website is **fully responsive**, ensuring a smooth experience on both **desktop and mobile devices**.  
  - Optimized for easy navigation and readability on different screen sizes.  

These features provide a **user-friendly**, **well-structured**, and **efficient** shopping experience for customers, ensuring they can easily explore, purchase, and interact with the farm’s products.

### Custom Features  

In addition to the core features inspired by **Boutique Ado**, the **Golden Hoof** website includes several custom enhancements to improve user experience and functionality.  

#### ⭐ Dynamic Product Rating System  
- Users can **rate products** dynamically, and the **average rating is updated in real-time**.  
- Ratings influence **sorting by rating**, ensuring that higher-rated products appear first.  
- Customers can submit a **star rating without a review**, which still affects the overall product rating.  

#### 📝 Customer Reviews  
- Users can leave **detailed product reviews** along with a rating.  
- The latest reviews are **displayed dynamically on the homepage**, providing fresh user feedback.  
- Each customer can **only review a product once**, ensuring authenticity.  

#### 📩 Contact Form with Admin Panel Integration  
- A **dedicated contact form** allows customers to send inquiries or feedback directly to the site administration.  
- Administrators can access a **custom admin panel** with all submitted messages.  
- Messages can be **reviewed and deleted** by the admin when necessary.  

These custom features provide a **more interactive and user-friendly** experience, making **Golden Hoof** stand out as a well-rounded e-commerce platform.  



## Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository

Clone the project from GitHub and navigate into the project directory:

```bash
git clone https://github.com/TeRRaeB/Project_5.git
cd Project_5
```


### 2. Install Python Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

This installs all dependencies listed in `requirements.txt`.


### 3. Create the `env.py` File

In the root directory of the project, create a new file named `env.py`. This file will hold your environment variables.

**Add the following environment variables to `env.py`:**

```python
import os

os.environ['STRIPE_PUBLIC_KEY'] = 'your_stripe_public_key'
os.environ['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'
os.environ['STRIPE_WH_SECRET'] = 'your_stripe_webhook_secret'
os.environ['SECRET_KEY'] = 'your_django_secret_key'
os.environ['DATABASE_URL'] = 'your_database_url'
os.environ['AWS_ACCESS_KEY_ID'] = 'your_aws_access_key_id'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_aws_secret_access_key'
os.environ['AWS_S3_REGION_NAME'] = 'your_aws_region'
os.environ['AWS_STORAGE_BUCKET_NAME'] = 'your_aws_bucket_name'
os.environ['USE_AWS'] = 'True'  # Set to 'False' if you are not using AWS for static file storage
```

> **Note:** You can generate new keys for **Stripe** and **AWS** in their respective dashboards.

### 4. Set Up the Database

Before running the project, ensure that your database is set up. If you're using PostgreSQL, you'll need to create a database and apply migrations. Run the following commands to set up your database:

```bash
python manage.py migrate
```

This will apply all the migrations and set up the required database tables.

### 5. Collect Static Files

If you're using static file storage (especially AWS S3), you'll need to collect all static files with the following command:

```bash
python manage.py collectstatic
```

This command will collect all static files into the directory specified in your Django settings.

### 6. Run the Development Server

Once everything is set up, you can start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the project.

### 7. Create a Superuser (Optional)

If you want to access the Django admin panel, create a superuser with the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser credentials (username, email, password).

---

## Deployment to Heroku

1. **Prepare your code**:
    - Make sure all dependencies are listed by running:
      ```bash
      pip freeze > requirements.txt
      ```
    - Create a `Procfile` in the root of your project:
      ```bash
      web: gunicorn golden_hoof.wsgi
      ```
2. **Push changes to GitHub**:
    ```bash
    git add .
    git commit -m "Prepare for Heroku deployment"
    git push
    ```

3. **Create and configure Heroku app**:
    - Log in to Heroku and create a new app.
    - Choose a unique app name and region.
    - Go to **Resources → Add-ons** and search for **Heroku Postgres**. Add it.

4. **Set environment variables** in **Settings → Reveal Config Vars**:
    - `SECRET_KEY`
    - `STRIPE_PUBLIC_KEY`
    - `STRIPE_SECRET_KEY`
    - `STRIPE_WH_SECRET`
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `AWS_STORAGE_BUCKET_NAME`
    - `USE_AWS = True`
    - `DATABASE_URL` is added automatically

5. **Allow Heroku in Django settings**:
    ```python
    ALLOWED_HOSTS = ['golden-hoof.herokuapp.com']    
    ```
6. **Deploy from GitHub**:
    - Go to **Deploy** tab.
    - Choose **GitHub** as deployment method.
    - Connect your repo and enable auto deploys or manually deploy branch.

7. **View the deployed app**:
    - Once deployed, click **View** to open your live site.

---

## Testing

### HTML 
[W3C HTML validator](https://validator.w3.org/)
HTML index
![HTML index valid](/doc/valid-html.png)
Product add
![HTML "Product add" valid](/doc/valid-html-2.png)
Bag page
![HTML "Bag page" valid](/doc/valid-html-3.png)
All Products
![HTML "Products page" valid](/doc/valid-html-4.png)


### CSS
[W3C CSS validator](https://jigsaw.w3.org/css-validator/)

![CSS valid](/doc/valid-css.png)

### Lighthouse
[Lighthouse App Chrome](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)

**slow download speed due to remote database**

![Lighthouse valid](/doc/valid-lighthouse.png)

### Responsiveness Testing

Testing for responsiveness was conducted using Chrome Dev Tools. The website was tested extensively on a range of emulated mobile, tablet and large format screen sizes in both portrait and landscape orientations.

| Device |  Resolution  |   Result  |        
| ------------------ | ------------- | ------------- |
| Samsung Galaxy S8+|  360 x 740  |   Pass  |
| iPhone 6/7/8 |  375 x 667  |   Pass  |
| iPhone X |  375 x 812  |   Pass  | 
| iPhone 12 PRO |  390 x 844  |   Pass  |
| Samsung Galaxy A51/71 |  412 x 914  |   Pass  |
| iPhone XR |  414 x 896  |   Pass  | 
| iPad Mini |  768 x 1024  |   Pass  | 
| iPad Air |  820 x 1180  |   Pass  | 
| iPad Pro |  1024 x 1366 |   Pass  | 
| HP Laptop 14s |  1920 x 1080|   Pass  | 
 
### Manual Testing

Manual testing was conducted to verify the functionality, usability, and reliability of the application across various user scenarios, including user interactions, payment processing, and error handling. The tests ensured that all features work as expected in real-world conditions on multiple browsers (Chrome, Firefox, Safari) and devices.

#### Objectives
- Validate end-to-end user flows (e.g., registration, product browsing, checkout).
- Confirm integration with external services, such as Stripe for payments.
- Test error handling for edge cases (e.g., invalid inputs, empty cart).
- Ensure the admin panel supports all required operations.

#### Test Scenarios
The following scenarios were manually tested to cover critical functionality:

| Feature | Scenario | Steps | Expected Result | Status |
|---------|----------|-------|-----------------|--------|
| **User Authentication** | User registration | 1. Navigate to `/accounts/signup/`. <br> 2. Enter valid email, username, and password. <br> 3. Submit the form. | User is registered, redirected to login page, and receives a confirmation message. | Pass |
| **User Authentication** | User login | 1. Navigate to `/accounts/login/`. <br> 2. Enter valid credentials. <br> 3. Submit the form. | User is logged in and redirected to the homepage. | Pass |
| **User Authentication** | Invalid login | 1. Navigate to `/accounts/login/`. <br> 2. Enter incorrect credentials. <br> 3. Submit the form. | Error message: "Invalid username or password." | Pass |
| **Product Management** | View product list | 1. Navigate to `/products/`. <br> 2. Browse product listings. | All products are displayed with correct names, prices, and images. | Pass |
| **Product Management** | Add product (admin) | 1. Log in as superuser. <br> 2. Navigate to `/products/add/`. <br> 3. Add a new product with category, subcategory, name, description, price, and image. | Product is added and visible on `/products/`. | Pass |
| **Shopping bag** | Add item to bag | 1. Navigate to a product page. <br> 2. Click "Add to bag." | Item is added to bag, and bag icon updates with item count. | Pass |
| **Shopping bag** | Empty cart checkout | 1. Navigate to `/bag/`. <br> 2. Attempt checkout with an empty cart. | Error message: "Your bag is empty." | Pass |
| **Checkout & Payment** | Successful payment | 1. Add items to cart. <br> 2. Navigate to `/checkout/`. <br> 3. Enter valid Stripe test card details (e.g., 4242 4242 4242 4242). <br> 4. Submit payment. | Payment is processed, user is redirected to a success page, and order is recorded. | Pass |
| **Checkout & Payment** | Failed payment | 1. Add items to cart. <br> 2. Navigate to `/checkout/`. <br> 3. Enter invalid card details. <br> 4. Submit payment. | Error message from Stripe: "Invalid card details." | Pass |
| **Error Handling** | Access non-existent page | 1. Navigate to `/nonexistent/`. | Custom 404 error page is displayed. | Pass |
| **Error Handling** | Server error simulation | 1. Simulate a server error (e.g., misconfigured database). | Custom 500 error page is displayed. | Pass |


#### Testing Environment
- **Browsers**: Chrome (latest), Firefox (latest).
- **Device**: Desktop (1920x1080)
- **Network Conditions**: Tested with both high-speed Wi-Fi and throttled 3G to simulate real-world scenarios.

#### Stripe Integration Testing
- **Test Cards**: Used Stripe’s test card numbers (e.g., `4242 4242 4242 4242` for success, `4000 0000 0000 0002` for failure).
- **Webhooks**: Verified that Stripe webhooks correctly update order statuses (e.g., payment succeeded, payment failed).
- **Security**: Ensured sensitive data (e.g., card details) is not stored in the database.

#### Observations
- All user flows worked as expected, with intuitive navigation and clear feedback.
- Stripe payments were processed reliably, with proper error handling for invalid inputs.
- Custom error pages (404, 500) rendered correctly and provided user-friendly messages.
- The admin panel was fully functional for CRUD operations on products, users, and orders.

## Known Issues & Troubleshooting

### 1. Database Migration from SQLite3 to PostgreSQL
**Problem:** Initially, the project was started using SQLite3 as the database. Later, the project was migrated to PostgreSQL. JSON and SQL dumps were created for the data migration, but they couldn't be imported successfully due to errors during the process. As a result, product data had to be uploaded again manually to the site.

**Solution:** After facing import issues, the data was re-uploaded manually to ensure the proper functioning of the application. It is recommended to use PostgreSQL from the start to avoid these issues with data migration.

### 2. Dependency Issues on Heroku Deployment
**Problem:** While deploying the project to Heroku, some dependencies in the `requirements.txt` file had to be updated. Specifically, the version numbers had to be changed from `==version` to `>=version` to avoid version conflicts. Additionally, the `Profiles` app required a newer version of `django-countries` (version `>=7.6.1`).

**Solution:** To resolve these issues, the dependencies were updated in the `requirements.txt` file, and the necessary changes were made to ensure compatibility with Heroku. It is advised to regularly check for updates to dependencies when deploying to different environments.


## Future Enhancements

### Ability to Add Photos with Reviews:
- Users will be able to upload photos along with their product reviews. This feature will allow customers to share images of the products in use, enhancing trust and providing more context.
- Implementation Steps:
  - Add a file upload field to the review form.
  - Handle image uploads on the server-side.
  - Display uploaded photos alongside the reviews on the product page.

 

### Add "Recommended Products for You" Based on Previous Purchases:
- The system will analyze the user's purchase history and recommend products they are likely to be interested in. This can be done by:
  - Storing users' purchase history in the database.
  - Implementing an algorithm to recommend products based on past purchases.
  - Displaying recommended products on the homepage or user profile page.

 

### Display "Recommended Products" Based on Reviews and Ratings (e.g., products with ratings of 4.7 or higher):
- To enhance product recommendations, display items with high ratings. This will help build trust among users.
  - Filter products with ratings of 4.7 and higher.
  - Show these products on the homepage or in a dedicated "Recommended Products" section.
  - Consider creating a page for popular products with good reviews.
 
## Credits

This project utilizes the following technologies and resources:

- **Django**: A high-level Python web framework used for building the web application.
- **Bootstrap**: A popular front-end framework for building responsive, mobile-first websites.
- **Amazon S3**: Used for storing and serving images.
- **Stripe**: Payment processing service integrated for handling transactions.
- **Heroku**: Platform as a Service (PaaS) used for deploying and hosting the application.
- **Mailchimp**: Used for email marketing and communication with users.
- **Bing AI Image Generator**: All images on this website were generated using Bing's AI-powered image generator.
- **Font Awesome**: A toolkit for adding vector icons and social logos to the website.
- **Favicon.io** used to create favicon.


Inspired by the **Boutique Ado** project, this application aims to provide a seamless shopping experience for users, showcasing high-quality farm products.

Special thanks to all the technologies and services that made this project possible!