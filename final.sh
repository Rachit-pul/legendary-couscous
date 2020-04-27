#!/bin/bash
while :
do
echo ""
echo "***Phone Directory***"
echo "1.Add Contact"
echo "2.Search Contact"
echo "3.Delete Contact"
echo "4.View Phone Directory"
echo "5. Quit"
read -p "Enter your choice : " usr_cmd
clear

case $usr_cmd in
	1)read -p "Enter  Name of Contact to be added" name
	  read -p "Enter Number" number
	  clear
	  echo "-> Name:$name. ->Number:$number"
	  echo "$name : $number" >> phonedir.log
	  echo "Saved Successfully";;
	2)read -p "Enter contact name" search_name
	  echo "Search Result"
	  grep -i $search_name phonedir.log
	  ;;
	3)read -p "Enter contact name to be delete(case sensitive)" delete_string
	  sed -i -e "/$delete_string/d" phonedir.log
	  echo "Delete Successful"
	  ;;
	4)echo "Phone Directory"
	  echo ""
	  cat phonedir.log
	  ;;
	5)break
	  ;;
	*) echo "INVALID OPTION"
esac;
done
