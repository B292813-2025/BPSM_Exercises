cat mock_NCBI.fasta | awk 'BEGIN{count=0;} {
if(substr($1,1,1)==">"){
	if(count==0){
		printf $1"\n";}
	else{ 
		printf "\n"$1"\n";}
count++; }
	else{
	printf $1; } 
}
END{printf "\n";}' > singleline_NCBIseqs.fasta

