# Puppet script to increase limit to file limits.conf.

exec { 'update limits':
  command => "/usr/bin/sudo /bin/sed -i 's/5/8192/g; s/4/9126/g' /etc/security/limits.conf",
}
