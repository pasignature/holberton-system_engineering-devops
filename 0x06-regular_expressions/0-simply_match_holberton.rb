#!/usr/bin/env ruby

# script accepts one argument and pass it to a regexp matching method
puts ARGV[0].scan(/(Holberton\w?)/).join
