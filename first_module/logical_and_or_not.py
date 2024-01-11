is_has_good_amount = True;
is_has_good_TK=True;
is_has_criminal_record = False;
if is_has_good_amount and is_has_good_TK:
    print("Today you can buy products");
else: print("No you can't buy products");

if is_has_good_amount or is_has_good_TK:
    print("You have one option. you can buy everything!")
else:
    print("No, you can't buy anything!");

if is_has_good_amount and not is_has_criminal_record:
    print("Your are the good person so you can buy the products")
else:
    print("no")