#!/usr/bin/env ruby

# regex to match 10 digit phone number \(\d{3}\)\s\d{3}-\d{4}
puts ARGV[0].scan(/\b\d{10,10}\b/).join
