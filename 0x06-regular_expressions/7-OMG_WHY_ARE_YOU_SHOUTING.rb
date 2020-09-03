#!/usr/bin/env ruby

#regex to match all caps oly - am i shouting?
puts ARGV[0].scan(/[A-Z]/).join
