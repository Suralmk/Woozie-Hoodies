<h1 align="center">Woozie Hoodie and T-Shirt Store</h1>

###

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jest/jest-plain.svg" height="40" alt="jest logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" height="40" alt="django logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" height="40" alt="redis logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="40" alt="postgresql logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://github.com/Suralmk/Woozie-Hoodies/blob/main/shop/static/img/pngegg%20(16).png" height="40" alt="celery logo"  />
</div>

###

<br clear="both">

<div align="center" width="100%" height="auto" > 
  <img height="300" src="https://github.com/Suralmk/Woozie-Hoodies/blob/main/shop/static/img/gihub.png"  />
</div>

###

<h2 align="left">Description</h2>

###

<p align="left">Woozie is an e-commerce  website built in Django. It uses Redis as a cache backend and celery as a message queue  basically for sending pdf receipt invoices via email, but celery can be implemented to perform asynchronous task outside  of the HTTP request and response cycle. Django Allauth is used as an authentication framework and also serves the social authentication with Facebook and Google.</p>

###

<h2 align="left">Apps</h2>

###

<table>
  <tr>
    <th>Shop</th>
    <td>All the shop related views, product detail and list are included in this app including authenticating.</td>
  </tr>
  <tr>
    <th>Cart</th>
    <td>This is where the implementation of redis comes in and used for cached session to store the cart items.</td>
  </tr>
  <tr>
    <th>Order</th>
    <td>Order app is used to create orders and send the receipt of unpaid invoices via email using celery. If a user succesfully orders an item it will be saved in the database with status of Unpaid until they pay or they delete it.</td>
  </tr>
  <tr>
    <th>Payment</th>
    <td>This app is where payment is handled and the response from the webhook is recieved. Also when a customer pays succesfully a receipt with paid status including all of the items they have bought will be send via email using celery.</td>
  </tr>
</table>



###

<h2 align="left">Payment</h2>

###

<p align="left">I have integrated chapa's payment gateway which allow to receive money from local banks and also  using international cards including  paypal.</p>

###

## Installation

Clone the github repository

```bash
  git clone https://github.com/Suralmk/Woozie-Hoodies.git

  cd Woozie-Hoodies
```

Considering you already have docker instalelld

```bash
  docker-compose up --build
```

Open browser and run


```bash
  0.0.0.0:8000
```

<h2 align="left">Author</h2>

###

<p align="left">Surafel Melaku</p>

###

<div align="left">
  <a href="https://linkedin.com/in/surafel-melaku-298421235" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg" width="52" height="40" alt="linkedin logo"  />
  </a>
</div>

###
