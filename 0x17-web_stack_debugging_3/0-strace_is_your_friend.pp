# replace phpp with php

exec { 'fix-php':
   command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
   path    => '/usr/local/bin/:/bin/'
}
