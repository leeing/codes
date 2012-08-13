#!/usr/bin/perl -w
# set : A-B

use strict;
   
open(SA,"sa.txt") or die($!);
open(NIM,"nim_host2") or die($!);

my @sahost=<SA>;
my @nims=<NIM>;

chomp(@sahost);
chomp(@nims);

close(SA);
close(NIM);

print "the size of sahost is ($#sahost+1).\n";

my %samap;

foreach(@sahost){
	s/ //sig;
        if (exists $samap{$_}){
                print "The repeat of sa is $_\n";
        }else{
                $samap{$_} = 1;
        }
}


my %nimap;

#Check if there is any elemnet repeated in the nimed machines.
foreach(@nims){
	s/ //sgi;
	if (exists $nimap{$_}){
		print "The repeat of nims is $_\n";
	}else{
		$nimap{$_} = 1;
	}
}

#Check
foreach(@nims){
	s/ //sgi;
	if (! exists $samap{$_}){
		print "$_ is not in the nim list.\n";
	}	
}

print "the SA hosts not in NIM:\n";
foreach(@sahost){
	s/ //sgi;
	if (! exists $nimap{$_}){
		print $_ . "\n";
	}
}
