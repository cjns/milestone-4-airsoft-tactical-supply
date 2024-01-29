# Milestone 4: Airsoft Tactical Supply

## User Stories
### Viewing & Navigation
| User Story ID | As a/an | I want to be able to...                         | So that I can |
| ------------- | ------- | ----------------------------------------------- | --------------------------------------------------------------------------------------|
| 1             | Shopper | View a list of products                         | Select purchases |
| 2             | Shopper | View product categories                         | Find products quickly|
| 3             | Shopper | View details & specifications for each product  | Identify price, description, product image, and specifications |
| 4             | Shopper | View the total of my purchases at any time      | Avoid over spending |

### Registration & User Accounts
| User Story ID | As a/an   | I want to be able to...                         | So that I can                                                                           |
| ------------- | --------- | ----------------------------------------------- | --------------------------------------------------------------------------------------- |
| 5             | Site User | Register for an account                         | Have a personal account and view my profile                                             |
| 6             | Site User | Login or logout                                 | Access my personal account information                                                  |
| 7             | Site User | Recover my password                             | Recover access to my account                                                            |
| 8             | Site User | Receive an email confirmation after registering | Verify that my account registration was successful                                      |
| 9             | Site User | Have a user profile                             | View my personal order history and order confirmations, and save my payment information |

### Sorting & Searching
| User Story ID | As a/an | I want to be able to...                             | So that I can                                                                              |
| ------------- | ------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 10            | Shopper | Sort the list of available products                 | Identify the best priced and categorically sorted products                                 |
| 11            | Shopper | Sort a specific product category                    | Find the best priced in a specific category, or sort the products in that category by name |
| 12            | Shopper | Sort multiple categories of products simultaneously | Find the best-priced products across broad categories, such as 'rifles', or 'pistols'      |
| 13            | Shopper | Search by product name or description               | Find a specific product I'd like to purchase                                               |
| 14            | Shopper | See search results and the number of results        | Quickly decide whether the product I want is available                                     |

### Purchasing & Checkout
| User Story ID | As a/an | I want to be able to...                                     | So that I can                                       |
| ------------- | ------- | ----------------------------------------------------------- | ----------------------------------------------------|
| 15            | Shopper | Select the product quantity                                 | Ensure I don't accidentally select the options      |
| 16            | Shopper | View the items in my cart                                   | Identify the total cost                             |
| 17            | Shopper | Adjust the quantity of individual cart items                | Make changes to my purchase(s) before checkout      |
| 18            | Shopper | Enter my payment information                                | Check out without issue                             |
| 19            | Shopper | Feel my personal and payment information is safe and secure | Provide the required information to make a purchase |
| 20            | Shopper | View a confirmation order                                   | Verify that the information is correct              |
| 21            | Shopper | Receive an email confirmation once checkout is complete     | Maintain a record                                   |

### Admin & Store Management
| User Story ID | As a/an     | I want to be able to... | So that I can              |
| ------------- | ----------- | ----------------------- | ---------------------------|
| 22            | Store Owner | Add products            | Add new items              |
| 23            | Store Owner | Edit/Update a product   | Change product information |
| 24            | Store Owner | Delete a product        | Remove items               |

## Data Models
### Checkout models
### Products models

## Styling
### Fonts
System fonts:
- system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

![fonts](media/fonts.png)

Pros:
- User does not need to download the font.
- No need to self host.
- [Fast](https://www.cloudflare.com/en-gb/learning/performance/more/website-performance-conversion-rates/).
- [Avoid GDPR issues](https://www.cookieyes.com/documentation/google-fonts-and-gdpr/#:~:text=According%20to%20GDPR%2C%20an%20IP,party%20services%20without%20user%20consent.)

Cons:
- Not as unique.

## Technology
- HTML
- CSS
[- Bootstrap](https://getbootstrap.com/)
- JavaScript
- Python
[- Django](https://www.djangoproject.com/)

## Resources
- [Unsplash](https://unsplash.com)
- [Kevin Powell: These font stacks will improve your site performance](https://www.youtube.com/watch?v=VOd6jfAImV4)
- Code Institute
- [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/e3c29afef63a8e5a8dae3fdc6b1277eb32206dbc/media)
- [Land Warrior Airsoft](https://www.landwarriorairsoft.com/)
- [Airsoftdirect.uk.com](https://airsoftdirect.uk.com/)
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
- [Django](https://docs.djangoproject.com/en/3.2)
- [miniWebtool django secret key generator](https://miniwebtool.com/django-secret-key-generator/)

## Deployment & Local Development
VSCode and Github Desktop were used for local development and pushing code to GitHub.
### GitHub
### Steps for Forking the Github Repository
1. Log into GitHub.
2. Go to the Kartilo repository.
3. Select the 'Fork' button in the top right corner under your profile icon.
### Steps for Making a Local Clone
1. Log into GitHub.
2. Navigate to the repository you want to clone.
3. Select the '<> Code' and copy the link for your preferred method of cloning the site.
4. Use your terminal to navigate to the working directory you want use.
5. Type git clone into the terminal and paste the link you copied in step 3 and press enter.
### Database: Elephant SQL
1. Log/sign into Elephant SQL.
2. Create a new team.
3. Create new instance.
4. Select your required plan.
5. Select your region/closest data center.
6. Review your details and create the instance.
7. Return to the dashboard, click the database instance you have created, and store the database URL.
### Heroku
1. Login into Heroku.
2. Create and name a new app.
3. Enter settings, reveal and populate the config vars.
4. Click Deploy and select a deployment method of your choosing.
5. Click 'More' and run the console.
6. Type 'python' in the console and click 'run'.
7. Enter the following into the termainl.
   - from <yourappname> import app, db
   - app.app_context().push()
   - db.create_all()
8. Exit the terminals with 'exit()'.
9. Click 'Open app' to view your app.