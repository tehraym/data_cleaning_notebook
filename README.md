# Data Cleaning & Exploring Key Metrics for Property Investors/Buyers in Kuala Lumpur city

## Foreword
When exploring investment prospects in Malaysia, property investment stands out as a compelling option.
Malaysia is well-known for its accommodating mortgage policies, permitting Malaysian citizens to obtain financing of up to 90% for their initial two residential properties. Additionally, the country's property market offers a wide array of options, catering to diverse investment preferences and strategies. Whether one is interested in residential condominiums or landed developments, investors have abundant choices to diversify their portfolios and leverage emerging opportunities.

This notebook will cover 
- Loading the data up Jupyter Notebook using Pandas Library
- Features Formatting: Transforming the features making them suitable for analysis, modeling, or visualization
- Categorical Variables: Techniques for incorporating new categorical variables to enrich the dataset.
- Identifying and Handling Outliers: Methods for detecting and managing outliers in the property data.
- Preparing Data for Visualization: Steps to prepare the dataset for effective visualization and analysis.
- Summary Statistics for All Regions in Kuala Lumpur: An overview of summary statistics for each region in Kuala Lumpur.

For readers who prefer to focus on the insights and visualizations rather than the technical details of data preprocessing
Please feel free to skip ahead to No 6. Data Visualization

## Disclaimer: Use of WebScraped Data
The data presented on this platform has been obtained through web scraping, a process of extracting information from websites using [Playwright](https://playwright.dev/python/), a browser automation tool.

## Data Collection Process: 
Web scraping involves automated extraction of data from websites using software tools or scripts. While we make efforts to adhere to website terms of service and legal guidelines, web scraping may be subject to legal restrictions or limitations imposed by website owners.

## Limitations and Risks:
Accuracy: The data used in this analysis do not necessarily reflect the current state of the property market.They have been sourced from property listing websites specifically for this analysis. It's important to note that certain locations may have insufficient data due to a lack of listings in those areas.
Example: When a region have lesser rows data, it does not mean that that area is not highly populated, it means that there is lack of listing in that region.

Intended Use: The data presented on this platform is for educational purposes only. It is intended to facilitate learning, research, and analysis. Any use of this data for illegal or unethical purposes, including but not limited to criminal activities, is strictly prohibited.

Usage and Reliability: Users are advised to exercise caution and independently verify the accuracy and reliability of the data before making decisions or relying on it for critical purposes. We disclaim any liability for damages or losses arising from the use of web scraped data.

By accessing or using the data presented on this platform, you acknowledge and agree to the terms of this disclaimer.