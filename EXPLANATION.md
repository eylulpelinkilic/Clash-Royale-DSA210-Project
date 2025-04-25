I fetched these data from my local machine, not from Colab. Thus, here are the codes that I used to fetch these data even though it is not supported by Colab. 
The key point here was that, I had a problem with calculating elixir rates for same decks. 
I found out that this was because elixir rates for some cards were not defined by default initially. 
That's why I additionally extracted the elixir data for all cards and filled the NaN values of the initial data with their actual values that I got from the card_elixir_costs.xlsx.
