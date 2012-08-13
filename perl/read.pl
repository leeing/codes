#!/usr/bin/perl -w

use strict;
   
open(SA,"sa_host") or die($!);
open(NIM,"nim_host2") or die($!);

my @sahost=<SA>;
my @nims=<NIM>;


foreach(@nims){
	print;
}
