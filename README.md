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
  - The overall product rating is calculated based on all submitted ratings and reviews.

- **User Authentication and Account Management**  
  - Secure **user registration and login** system.  
  - Logged-in users can manage their **profile**, view **order history**, and track purchases.  

- **Shopping Cart and Checkout**  
  - Users can **add products to the cart** and proceed to a **secure checkout**.  
  - The checkout process is designed to be user-friendly and efficient.

- **Contact and Support**  
  - A **Contact Us** page allows users to send inquiries and get assistance from the farm.  
  - Customers can find farm location details and business hours.

- **Mobile-Friendly and Responsive Design**  
  - The website is **fully responsive**, ensuring a smooth experience on both **desktop and mobile devices**.  
  - Optimized for easy navigation and readability on different screen sizes.

These features provide a **user-friendly**, **well-structured**, and **efficient** shopping experience for customers, ensuring they can easily explore, purchase, and interact with the farm’s products.

