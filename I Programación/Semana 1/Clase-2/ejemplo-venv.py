import easy_date
import cowsay

str_date = '25/12/2014' #%d/%m/%Y
new_str_date = easy_date.convert_from_string(str_date, '%d/%m/%Y', '%m-%d-%Y')

print(new_str_date)

cowsay.cow("Hola Mundo!")