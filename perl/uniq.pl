#!/usr/bin/perl -w 

# find the repeat lines in a file.

use strict;

open(SA,"sa_host") or die($!);

my @sahost=<SA>;

print "the size of sahost is ($#sahost+1).\n";

my %samap;

foreach my $sa(@sahost){
	if (exists $samap{$sa}){
		print "The repeat one is $sa\n";	
	}else{
		$samap{$sa} = 1;
	}
}


