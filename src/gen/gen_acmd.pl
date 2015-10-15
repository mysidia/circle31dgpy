#!/usr/bin/perl

open T, ">interpreter.cmdfuns.h";

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
		if ($line =~ /^CMD_FUN\((\S+)\)/) {
			printf T "ACMD(" . $1 . ");\n";
		}
	}
	print T "\n";
}

print T "/* ++AUTO-GENERATED++ Do Not Edit*/\n";
gen_stuff("interpreter.c");
