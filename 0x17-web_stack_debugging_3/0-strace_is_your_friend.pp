# replace phpp with php

exec { 'fixPhp':
provider => shell,
command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
