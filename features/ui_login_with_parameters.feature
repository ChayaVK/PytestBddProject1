Feature: UI Login Functionality with parameters
  As a valid user
  I want to log in to the application
  So that I can access my account

Scenario Outline: Login functionality
      Given user lands on to login page
      When user enter <username> and <password>
      Then user should be able to see right <uimessage>

  Examples:
  |username | password | uimessage |
  |tomsmith | SuperSecretPassword! | You logged into a secure area!|
  |tomsmith | rthfhn               | Your password is invalid!     |
  |chaya    | SuperSecretPassword! | Your username is invalid!     |
  |chaya    | fhgfjytty            | Your username is invalid!     |