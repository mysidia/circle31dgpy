#!/usr/bin/perl

open T, ">pydefs.h";

sub gen_stuff
{	
	my $fn = shift;

	open(F,"<" . $fn);
	$i = 1;

	while($line = <F>)
	{
		chomp($line);
		if ($line =~ /\"/) {
			next;
		}
		if ($line =~ /^#define ([^\s\(]+)\s/) {
			if ($1 eq "log" || $1 eq "RL_SEC" || $1 eq "core_dump"
		            || $1 eq "NULL" || $1 eq "CONFIG_OK"
			    || $1 eq "CONFIG_NOPERSON" || $1 eq "CONFIG_DFLT_IP"
		            || $1 eq "CONFIG_NOEFFECT" || $1 eq "CONFIG_DFLT_DIR"
			    || $1 eq "CONFIG_LOGNAME"  || $1 eq "CONFIG_MENU"
	    		    || $1 eq "CONFIG_WELC_MESSG" || $1 eq "CONFIG_START_MESSG"
			    || $1 eq "QNRM" || $1 eq "QRED" || $1 eq "QGRN" 
			    || $1 eq "QYEL" || $1 eq "QBLU" || $1 eq "QMAG"
			    || $1 eq "QCYN" || $1 eq "QWHT"
		    	)
			    {next;}

			printf T "%-30s", "_C($1) ";
			if ($i % 3 == 0) { print T "\n"; }
			$i++;
		}
	}
	print T "\n";
}

print T "/* ++AUTO-GENERATED++ Do Not Edit*/\n";
gen_stuff "utils.h";
gen_stuff "structs.h";
gen_stuff "spells.h";
gen_stuff "screen.h";
