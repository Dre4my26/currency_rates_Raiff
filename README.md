# Currency_rates_Raiff
5-min parser to parse **currency rate** from Raiffeisen Bank, 
**save** it to CSV file (maybe one day I will find a way to use it) and 
**notify** me via TelegramBot if the rate is higher than some value.

## How to use:
Simply run the script via almost any IDE to get text line with time and rate.

#### In case you want to change the currency:
Simply change
- *"Евро"* => *"США"* (USD)
- *"Евро"* => *"стерлингов"* (GBP)
- *"Евро"* => *"иена"* (JPY)
- *"Евро"* => *"юань"* (CNY)
 
    in the main() function if you want to 
    get the rate of other currency.

### TODO:
- TeleBot service to notify me in case Euro is higher than some value I want