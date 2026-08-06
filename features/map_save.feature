Feature: Check out and save the maps
  Scenario: Save the 24 hour precipitation and current temperature map
    Given open the main page of idokep.hu
    When go to precipitation map page
    And see the precipitation map for the last 24 hours
    Then save the image of the precipitation map

    When go to heat map page
    And view the current heat map
    Then save the image of the heat map