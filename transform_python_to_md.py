a = {
  "head size": {
	"examples" : [
	  "Head size My head size is 2.2mm",
	  "My head size is 6cm",
	  "his head size is 22cm",
	  "her head size is 32cm"
  ],
	"xrange" : ["2.2mm", "6cm", "22cm", "22cm", "32cm"]
  },
  "favorite holiday": {
	"examples" : [
	  "Favorite holiday My favorite holiday is Halloween",
	  "he said his favorite holiday is veterans day",
	  "my wife's favorite holiday is thanks giving day"
  ],
	"xrange" : ["halloween", "veterans_day", "thanks_giving_day"]
  }
}

def transform_python_dict_to_md_format(dict_object, output_file_path="output.md"):
    output_file = open(output_file_path, "w+")  # w+ stands for create or overwrite
    for intent, training_data in dict_object.items():
        entities = training_data.get("xrange", list())  # I prefer safe accessor all the time
        examples = training_data.get("examples", list())
        output_file.write(f"## intent:{intent}\n")  # I hope you're familiar with [F-Strings](https://www.python.org/dev/peps/pep-0498/), only works with Pyhon 3.6 +
        for example in examples:  # As I said, I wrote this so fast so NoQA
            for entity in set(entities):  # You have repeated entities (xranges)
                # Ideally you should have an entity_name (instead of intent) for each entity, but that should do the work
                # Also as you're using composite entities, I have to do some tricky steps to match the "_" to " " 
                example = f"[{entity}]({intent})".join(example.lower().split(entity.replace("_", " ")))  
                
            output_file.write(f"{example}\n")
        output_file.write("\n")

if __name__ == "__main__":
    transform_python_dict_to_md_format(a)