# Testing

## Tools
HTML: [W3C Markup Validator](https://validator.w3.org/)
CSS: [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
Accessibility: [WAVE (Web Accessibility Evaluation Tool)](https://wave.webaim.org/)
Performance: [Lighthouse (Within Chrome Developer Tools)](https://developer.chrome.com/docs/lighthouse/overview/)
Python Syntax: [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
JS Syntax: [ESLint](https://eslint.org/)

## Sending Emails
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+Q1_2020/courseware/4201818c00aa4ba3a0dae243725f6e32/1319d50e2bdb4defa4226fe6db5d57a3/?child=first
When trying to send actual emails from your IDE, an error stating Issue binding port will be displayed which causes sending of the email to fail. Logging issues to the terminal while developing in your IDE, as done in this video, serves to test Authentication and Authorisation functionality until project deployment.

Once deployed to Heroku, the sending of actual emails will become a possibility, so please wait until then before attempting it.

## Testing User Stories
## User Stories
### Viewing & Navigation
| User Story ID | As a/an | I want to be able to...                         | Evidence of meeting user story |
| ------------- | ------- | ----------------------------------------------- | --------------------------------------------------------------------------------------|
| 1             | Shopper | View a list of products                         | A link that displays all product |
| 2             | Shopper | View product categories                         | A link that displays products by category|
| 3             | Shopper | View details & specifications for each product  | A link that displays products by price |
| 4             | Shopper | View the total of my purchases at any time      | Access to cart |

### Registration & User Accounts
| User Story ID | As a/an   | I want to be able to...                         | Evidence of meeting user story                   |
| ------------- | --------- | ----------------------------------------------- | --------------------------------------------------------------------------------------- |
| 5             | Site User | Register for an account                         | Registration page                                             |
| 6             | Site User | Login or logout                                 | Login/logout functionality                                                  |
| 7             | Site User | Recover my password                             | Future implementation (set up email functionality)                                             |
| 8             | Site User | Receive an email confirmation after registering | Future implementation (set up email functionality)                                      |
| 9             | Site User | Have a user profile                             | User profile present |

### Sorting & Searching
| User Story ID | As a/an | I want to be able to...                             | Evidence of meeting user |
| ------------- | ------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 10            | Shopper | Sort the list of available products                 | Sorting implemented                                |
| 11            | Shopper | Sort a specific product category                    | Categorical listing implemented |
| 12            | Shopper | Sort multiple categories of products simultaneously | Ability to list all categories      |
| 13            | Shopper | Search by product name or description               | Search feature implemented                                               |
| 14            | Shopper | See search results and the number of results        | Implemented on product search page                                     |

### Purchasing & Checkout
| User Story ID | As a/an | I want to be able to...                                     | Evidence of meeting user story        |
| ------------- | ------- | ----------------------------------------------------------- | ----------------------------------------------------|
| 15            | Shopper | Select the product quantity                                 | Ability to update cart      |
| 16            | Shopper | View the items in my cart                                   | Cart feature implemented                             |
| 17            | Shopper | Adjust the quantity of individual cart items                | Item quantity can be increased/decreased      |
| 18            | Shopper | Enter my payment information                                | Implemented via Stripe                             |
| 19            | Shopper | Feel my personal and payment information is safe and secure | Authentication implemented |
| 20            | Shopper | View a confirmation order                                   | Confirmation order shown after purchase              |
| 21            | Shopper | Receive an email confirmation once checkout is complete     | Future implementation (set up email functionality)                                   |

### Admin & Store Management
| User Story ID | As a/an     | I want to be able to... | Evidence of meeting user story              |
| ------------- | ----------- | ----------------------- | ---------------------------|
| 22            | Store Owner | Add products            | Add to cart feature              |
| 23            | Store Owner | Edit/Update a product   | Store owner can edit/update products |
| 24            | Store Owner | Delete a product        | Ability to remove items             |

## File Validation
### Python Files
### HTML Files
### CSS Files
### JS Files

## Toasts
|Feature & Expected outcome|Testing|Result|Pass/Fail|
|-|-|-|-|
|Toast appears when adding item to cart|Add item to cart|Success message appears|Pass|
|Toast appears when adding additional item and thus increasing item quantity|Add additional item to cart|Success message appears|Pass|
|Toast appears when no search criteria added|Search without criteria|Error message appears|Pass|

## Webhooks
## Forms

### My Profile Form - pass
### Registration Form - pass
### Checkout Form - pass

|Feature & Expected outcome|Testing|Result|Pass/Fail|
|-|-|-|-|
|Checkbox that saves the delivery into to your profile|Place order, tick checkbox, and check profile info|Info. is updated|Pass|
|Webhook handles profiles if form submission fails|Comment out form submission code in stripe_elements.js and submit order|Order is still processed|Pass|
Confirmation email on purchase

## Product Management
|Feature & Expected outcome|Testing|Result|Pass/Fail|
|-|-|-|-|
|Add product with image|Add product with image|Product is added|Pass|
|Add product without image|Add product without image|Product is added|Pass|
|Edit product information|Updated fields for an existing product|Information updated|Pass|
|Delete product|Delete an existing product|Product deleted|Pass|

## Bugs
Once deployed, selecting the accessories product from the django admin returns a Bad Request(400).