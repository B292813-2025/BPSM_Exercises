splits = $((993686/100))0

split -l ${splits} Test_dataset.fa testing_eddie/split_reads_directory/
splitdir=${HOME}"/testing_eddie/split_reads_directory"

myfavouritesequence='ACATAAAACATCAAAGTGAACAGATTGTAGTGTAAGAAGTTAGATTAA' 
while read line
do read line2
 if [[ ${line2} == *${myfavouritesequence}* ]] ;
 then
  echo "The sequence was found in" ${line} ${line2}
 fi  
done < $1

