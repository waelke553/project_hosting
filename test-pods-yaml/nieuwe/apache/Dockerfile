FROM php:7.4-apache

# Set the working directory
WORKDIR /var/www/html

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libzip-dev \
    unzip

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql zip

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Enable Apache modules
RUN a2enmod rewrite

# Set ownership and permissions for the copied files
RUN chown -R www-data:www-data /var/www/html/ \
    && chmod -R 755 /var/www/html/


# Expose port 80
EXPOSE 80