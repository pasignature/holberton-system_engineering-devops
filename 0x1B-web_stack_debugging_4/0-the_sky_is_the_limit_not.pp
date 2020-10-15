# Puppet script to change data 15 to 10240

exec { 'update line':
  command => '/usr/bin/sudo /bin/sed -i "s/15/10240/g" /etc/default/nginx && service nginx restart'
}
