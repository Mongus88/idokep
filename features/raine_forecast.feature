Feature: Check out and save if it will rain
  Scenario: Save to a csv file whether it will rain in the next four days
    Given open the main page of idokep.hu
    When see if it rains in the next four days
    Then save the results to a csv file