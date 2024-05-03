<?xml version="1.0"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <!-- aquesta linia afegeix el <!DOCTYPE html> -->
    <xsl:output method="html" doctype-system="about:legacy-compat" />

    <xsl:template match="/">
        <html lang="ca">
            <head>
                <!-- aneu en cura de tancar totes les etiquetes... som al món XML! -->
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <link rel="stylesheet" type="text/css" href="style.css" />
                <title>Exemple de XSLT</title>
            </head>
            <body>
                <h2>Botiga <xsl:value-of select="shop/name"/></h2>
                <h3>Adreça: <xsl:value-of select="shop/address"/></h3>
                <h3>URL: 
                    <a target="_blank">
                        <xsl:attribute name="href">
                            <xsl:value-of select="shop/url"/>
                        </xsl:attribute>
                        <xsl:value-of select="shop/url"/>
                    </a>
                </h3>

                <xsl:for-each select="shop/stock/category">
                    <h4><xsl:value-of select="@name"/></h4>
                    <table>
                        <tr>
                            <th>Name</th>
                            <th>Brand</th>
                        </tr>
                        <xsl:for-each select="product">
                            <tr>
                                <td>
                                    <xsl:value-of select="name"/>
                                </td>
                                <td>
                                    <xsl:value-of select="brand"/>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </table>

                </xsl:for-each>

            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>