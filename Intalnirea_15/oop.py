"""
Model the following requirements using OOP.
A vacuum cleaner retailer wants to manage their models.
Requirements:
* they can support multiple vacuum cleaner manufacturers (e.g. Bosch, Electrolux, etc)
* each vacuum cleaner has the following fields:
	- model name
	- base power ( 500W at start )
* Bosch vacuum cleaners have an additional field
	- timer ( which can receive an integer value ) and if it is not set then it should return False

* each vacuum cleaner supports the following behavior
    - start: which will print the message 'Vacuum cleaner {model_name} has started consuming {power} W'
	- increase_power: increase base power with 100W for most models and 150W for Bosch.
	Trying to increase power above 1000 will raise an error:
	    'Can't raise power above 1000W. Invalid current power {}.'
	    Where {} will be replaced with the invalid calculated current power.
	- to JSON: returns json with model name, current power and timer value (json)

* Bosch model supports upgrades. it exposes the following behavior:
	- upgrade: raises power increase from 150w to 200w

Run script:
1. Create 2 vacuum cleaners: Bosch and Electrolux. Store the vacuum cleaners in a list.
2. Print vacuum cleaners information
3. Iterate through the vacuum cleaners and increase their power.
4. Print vacuum cleaners information
5. Iterate through vacuum cleaners, find Bosch and upgrade it.
6. Print vacuum cleaners information.
"""
