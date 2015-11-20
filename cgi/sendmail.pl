#!/usr/bin/perl

 use strict;
 use warnings;
 use MIME::Lite::TT::HTML;

 my %params;

 $params{name} = 'Frank';
 $params{mail} = 'Wiles';
 $params{mex} = '24.99';

 my %options;
 $options{INCLUDE_PATH} = '/path/to/templates';

 my $msg = MIME::Lite::TT::HTML->new(
            From        =>  'admin@example.com',
            To          =>  'frank@example.com',
            Subject     =>  'Your recent purchase',
            Template    =>  {
                                text    =>  'test.txt.tt',
                                html    =>  'test.html.tt',
                            },
            TmplOptions =>  \%options,
            TmplParams  =>  \%params,
 );

$msg->send();