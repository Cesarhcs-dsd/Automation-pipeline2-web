Feature:login 
  As a user i want to be able to loguin in my account


  Scenario: invalid user authentication
    Given the user "test@fakeemial.com" is trying to loguin with the password "123467"
    When the user clicks on the login button
    Then the system shoudl displays an error message 