#list the subject accession for all HSPs
IFS=$'\t'
blast="blastoutput2.out"

cut -f2 "$blast" >  sub_accesion.txt

#list the alignment length and percent ID for all HSPs
cut -f4,3 "$blast" > len_and_ID.txt

#show the HSPs with more than 20 mismatches
while read -r c1 c2 c3 c4 mismatch rest; do
	[[ "$c1" == \#* ]] && continue
	if [ "$mismatch" -gt 20 ]; then
		echo -e "$c1\t$c2\t$c3\t$c4\t$mismatch\t$rest"
	fi
done < "$blast" > gt20_mismatch.txt

#show the HSPs shorter than 100 amino acids and with more than 20 mismatches
while read -r c1 c2 c3 len mismatch rest; do
	[[ "$c1" == \#* ]] && continue
	if [[ "$mismatch" -gt 20 &&  "$len" -lt 100 ]]; then
		echo -e "$c1\t$c2\t$c3\t$len\t$mismatch\t$rest"
	fi
done < "$blast" > lt100_gt20.txt

#list the first 20 HSPs that have fewer than 20 mismatches
count=0
max=20

while read -r c1 c2 c3 c4 mismatch rest; do
	[[ "$c1" == \#* ]] && continue
	if [ "$mismatch" -lt 20 ]; then
                echo -e "$c1\t$c2\t$c3\t$c4\t$mismatch\t$rest"
		((count++))
        fi

	if [ "$count" -ge "$max" ]; then
		break
	fi
done < "$blast" > first20u20.txt

#how many HSPs are shorter than 100 amino acids?
count=0

while read -r c1 c2 c3 len rest; do
        [[ "$c1" == \#* ]] && continue
        if [ "$len" -lt 100 ]; then
                ((count++))
        fi

done < "$blast"
echo "$count" > lt_100_count.txt

#list the top ten highest (best) HSPs
grep -v '^#' "$blast" | sort -k11,11g -k12,12gr | head -n 10 > top_HSPs.txt

#list the start positions of all matches where the HSP Subject accession includes the letters string "AEI"
grep -v '^#' "$blast" | grep 'AEI' | cut -f9 > AEI_start.txt

#how many subject sequences have more than one HSP?
cut -f2 "$blast" | sort | uniq -d | wc -l > multi_hsp.txt

#what percentage of each HSP is made up of mismatches?
while read -r c1 c2 c3 len mismatch rest; do
    [[ "$c1" == \#* ]] && continue
    percentage=$(echo "scale=2; ($mismatch / $len) * 100" | bc)
    echo -e "$c1\t$c2\t$c3\t$len\t$mismatch\t$percentage%"
done < "$blast" > percent_mm.txt

#allocate HSPs into different groups based on their scores
while read -r c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 score; do
    [[ "$c1" == \#* ]] && continue

    if [ "$(echo "$score >= 350" | bc -l)" -eq 1 ]; then
        echo -e "$c1\t$c2\t$score" >> high_scoreHSP.txt
    elif [ "$(echo "$score >= 200" | bc -l)" -eq 1 ]; then
        echo -e "$c1\t$c2\t$score" >> medium_scoreHSP.txt
    else
        echo -e "$c1\t$c2\t$score" >> low_scoreHSP.txt
    fi
done < "$blast"
