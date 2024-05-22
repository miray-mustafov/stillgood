# StillGood
Resale platform enabling users to buy and sell second-hand items.


## Table of contents
* [Demo](#demo)
* [Setup](#setup)
* [Features](#features)

## Demo
[![thumbnail_alt](https://img.youtube.com/vi/jGtYaj06EzY/0.jpg)](https://www.youtube.com/watch?v=jGtYaj06EzY)

## Setup
#### Make sure:
- You have installed Python 3.8 or higher.
- You have a working internet connection.

### 1. Open a terminal in a folder and `clone` the repository:
```
git clone https://github.com/miray-mustafov/stillgood.git
```
### 2. Navigate to the project directory:
```
cd stillgood
```
### 3. Create a virtual environment:
```
python -m venv venv
```
### 4. Activate the virtual environment:
#### On Windows:
```
venv\Scripts\activate
```
#### On macOS/Linux:
```bash
source venv/bin/activate
```
### 5. Install the required packages:
```
pip install -r requirements.txt
```
To start the application, ensure you are **in the project directory** and the **virtual environment is activated**. Then run:
```
python manage.py runserver
```
### *Happy browsing at StillGood!*


## Features
#### 1. User Authentication and Authorization

#### 2. Create, Read, Update, Delete (CRUD) Operations
Users can add new products, view existing listings, update details, and delete products.

#### 3. Images upload
Allow users to upload images for products.

#### 4. Paginated Listings
Implement pagination for browsing product listings to enhance user experience and performance.

#### 5. Search and Filtering
Enable users to search for products based on category, title or both.  
Allow filtering of product listings by categories.

#### 6. User Profiles:
Profile Management: Users can view and edit their profile information.  
Save Favorites: Users can save products to their wishlist for future reference.

#### 7. Admin Panel:
Admin can manage categories, users, products.

#### 8.Template System:
Utilizes Django templates for dynamic content rendering.
