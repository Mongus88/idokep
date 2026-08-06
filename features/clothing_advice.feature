Feature: Check out and save the recommended clothes from idokep.hu
  Scenario: Save today's recommendations to a text file
    Given open the main page of idokep.hu
    When see what clothes it recommends today
    Then save the results to a text file