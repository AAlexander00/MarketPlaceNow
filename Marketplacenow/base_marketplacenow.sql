-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-05-2025 a las 04:26:23
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base_marketplacenow`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_compras`
--

CREATE TABLE `carrito_compras` (
  `ID_CARRITO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `ID_CATEGORIA` int(11) NOT NULL,
  `NOMBRE_CATEGORIA` char(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contiene`
--

CREATE TABLE `contiene` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_CARRITO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='un producto puede estar en muchos carritos de compras, y un ';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_producto`
--

CREATE TABLE `detalle_producto` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_VENDEDOR` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='un vendedor puede tener varios productos, varios de esos pro';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devolucion_de_venta`
--

CREATE TABLE `devolucion_de_venta` (
  `ID_DEVOLUCION` int(11) NOT NULL,
  `ID_USUARIO` int(11) NOT NULL,
  `ID_FACTURA` int(11) NOT NULL,
  `FECHA_DEVOLUCIUON` int(11) NOT NULL,
  `COMMENT_DEVOLUCION` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_de_venta`
--

CREATE TABLE `factura_de_venta` (
  `ID_FACTURA` int(11) NOT NULL,
  `ID_USUARIO` int(11) NOT NULL,
  `ID_DEVOLUCION` int(11) DEFAULT NULL,
  `ID_PAGO` int(11) NOT NULL,
  `ID_TRANSPORTADORA` bigint(20) NOT NULL,
  `FECHA_FACTURA` date NOT NULL,
  `VALOR_FACTURA` bigint(20) DEFAULT NULL,
  `GUIA_FACTURA` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_producto`
--

CREATE TABLE `factura_producto` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_FACTURA` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='un producto puede estar en muchas facturas y varias facturas';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_seguimiento`
--

CREATE TABLE `factura_seguimiento` (
  `ID_FACTURA` int(11) NOT NULL,
  `ID_SEGUIMIENTO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='un seguimiento debe estar en muchas facturas, y muchas factu';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodo_de_pago`
--

CREATE TABLE `metodo_de_pago` (
  `ID_PAGO` int(11) NOT NULL,
  `NOM_PAGO` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_CATEGORIA` int(11) NOT NULL,
  `NOMBRE_PRODUCTO` char(30) NOT NULL,
  `DESCRIPCION` char(200) DEFAULT NULL,
  `PRECIO` int(11) NOT NULL,
  `FECHA_PUBLICACION` date DEFAULT NULL,
  `DIAS_GARANTIA` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto_devuelve`
--

CREATE TABLE `producto_devuelve` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_DEVOLUCION` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='un producto puede que tenga muchas devolcuiones, y las devol';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `promociones`
--

CREATE TABLE `promociones` (
  `ID_PROMOCION` int(11) NOT NULL,
  `NOM_PROMOCION` varchar(50) NOT NULL,
  `ESTADO_DESCUENTO` blob NOT NULL,
  `FECHA_INICIO` date NOT NULL,
  `FECHA_EXPIRACION` date NOT NULL,
  `FACT_DESCUENTO` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicidad`
--

CREATE TABLE `publicidad` (
  `ID_PUBLICIDAD` int(11) NOT NULL,
  `ID_VENDEDOR` int(11) DEFAULT NULL,
  `TIPO_PUBLICIDAD` char(30) NOT NULL,
  `FECHA_INICIO` date NOT NULL,
  `FECHA_FIN` date NOT NULL,
  `COSTO` int(11) NOT NULL,
  `ESTADO_PUBLICIDAD` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `publicidad_producto`
--

CREATE TABLE `publicidad_producto` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_PUBLICIDAD` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='una publicidad debe mostar varios productos y un producto pu';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resenas`
--

CREATE TABLE `resenas` (
  `ID_RESENA` int(11) NOT NULL,
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_USUARIO` int(11) NOT NULL,
  `PUNTUACION` int(11) DEFAULT NULL,
  `COMENTARIO` char(100) DEFAULT NULL,
  `FECHA_RESENA` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seguimiento`
--

CREATE TABLE `seguimiento` (
  `ID_SEGUIMIENTO` int(11) NOT NULL,
  `NOMBRE_SEGUIMIENTO` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `se_promociona`
--

CREATE TABLE `se_promociona` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `ID_PROMOCION` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='un producto puede estar en muchas promociones y una promocio';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transportadora`
--

CREATE TABLE `transportadora` (
  `ID_TRANSPORTADORA` bigint(20) NOT NULL,
  `NOM_TRANSPORTADORA` varchar(40) NOT NULL,
  `TEL_TRANSPORTADORA` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `ID_USUARIO` int(11) NOT NULL,
  `ID_CARRITO` int(11) NOT NULL,
  `NOMBRES_USUARIO` char(30) NOT NULL,
  `CORREOE` varchar(30) NOT NULL,
  `CONTRASENA` varchar(30) NOT NULL,
  `DIRECCION` varchar(30) DEFAULT NULL,
  `TELEFONO` int(11) DEFAULT NULL,
  `FECHAREGISTRO` date NOT NULL,
  `token` varchar(255) NOT NULL,
  `token_expira` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

CREATE TABLE `vendedor` (
  `ID_VENDEDOR` int(11) NOT NULL,
  `DIRECCION_COMERCIAL` varchar(30) DEFAULT NULL,
  `TELEFONO_COMERCIAL` int(11) DEFAULT NULL,
  `FECHAS_REGIS_VENDEDOR` date DEFAULT NULL,
  `NOMBRE_COMERCIAL` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito_compras`
--
ALTER TABLE `carrito_compras`
  ADD PRIMARY KEY (`ID_CARRITO`);

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`ID_CATEGORIA`);

--
-- Indices de la tabla `contiene`
--
ALTER TABLE `contiene`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_CARRITO`),
  ADD KEY `FK_CONTIENE2` (`ID_CARRITO`);

--
-- Indices de la tabla `detalle_producto`
--
ALTER TABLE `detalle_producto`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_VENDEDOR`),
  ADD KEY `FK_DETALLE_PRODUCTO2` (`ID_VENDEDOR`);

--
-- Indices de la tabla `devolucion_de_venta`
--
ALTER TABLE `devolucion_de_venta`
  ADD PRIMARY KEY (`ID_DEVOLUCION`),
  ADD KEY `FK_DEVUELVE` (`ID_USUARIO`),
  ADD KEY `FK_FACTURA_SE_DEVUELVE2` (`ID_FACTURA`);

--
-- Indices de la tabla `factura_de_venta`
--
ALTER TABLE `factura_de_venta`
  ADD PRIMARY KEY (`ID_FACTURA`),
  ADD KEY `FK_FACTURA_SE_DEVUELVE` (`ID_DEVOLUCION`),
  ADD KEY `FK_PAGA_FACTURA` (`ID_PAGO`),
  ADD KEY `FK_REALIZA` (`ID_USUARIO`),
  ADD KEY `FK_TRANSPORTA_FACTURA` (`ID_TRANSPORTADORA`);

--
-- Indices de la tabla `factura_producto`
--
ALTER TABLE `factura_producto`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_FACTURA`),
  ADD KEY `FK_FACTURA_PRODUCTO2` (`ID_FACTURA`);

--
-- Indices de la tabla `factura_seguimiento`
--
ALTER TABLE `factura_seguimiento`
  ADD PRIMARY KEY (`ID_FACTURA`,`ID_SEGUIMIENTO`),
  ADD KEY `FK_FACTURA_SEGUIMIENTO2` (`ID_SEGUIMIENTO`);

--
-- Indices de la tabla `metodo_de_pago`
--
ALTER TABLE `metodo_de_pago`
  ADD PRIMARY KEY (`ID_PAGO`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`ID_PRODUCTO`),
  ADD KEY `FK_PERTENECE_A_UNA_CATEGORIA` (`ID_CATEGORIA`);

--
-- Indices de la tabla `producto_devuelve`
--
ALTER TABLE `producto_devuelve`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_DEVOLUCION`),
  ADD KEY `FK_PRODUCTO_DEVUELVE2` (`ID_DEVOLUCION`);

--
-- Indices de la tabla `promociones`
--
ALTER TABLE `promociones`
  ADD PRIMARY KEY (`ID_PROMOCION`);

--
-- Indices de la tabla `publicidad`
--
ALTER TABLE `publicidad`
  ADD PRIMARY KEY (`ID_PUBLICIDAD`),
  ADD KEY `FK_PAGA` (`ID_VENDEDOR`);

--
-- Indices de la tabla `publicidad_producto`
--
ALTER TABLE `publicidad_producto`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_PUBLICIDAD`),
  ADD KEY `FK_PUBLICIDAD_PRODUCTO2` (`ID_PUBLICIDAD`);

--
-- Indices de la tabla `resenas`
--
ALTER TABLE `resenas`
  ADD PRIMARY KEY (`ID_RESENA`),
  ADD KEY `FK_REGISTRA_RESENA` (`ID_USUARIO`),
  ADD KEY `FK_RESENAS_DEL_PRODUCTO` (`ID_PRODUCTO`);

--
-- Indices de la tabla `seguimiento`
--
ALTER TABLE `seguimiento`
  ADD PRIMARY KEY (`ID_SEGUIMIENTO`);

--
-- Indices de la tabla `se_promociona`
--
ALTER TABLE `se_promociona`
  ADD PRIMARY KEY (`ID_PRODUCTO`,`ID_PROMOCION`),
  ADD KEY `FK_SE_PROMOCIONA2` (`ID_PROMOCION`);

--
-- Indices de la tabla `transportadora`
--
ALTER TABLE `transportadora`
  ADD PRIMARY KEY (`ID_TRANSPORTADORA`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_USUARIO`),
  ADD KEY `FK_TIENE` (`ID_CARRITO`);

--
-- Indices de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`ID_VENDEDOR`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `contiene`
--
ALTER TABLE `contiene`
  ADD CONSTRAINT `FK_CONTIENE` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`),
  ADD CONSTRAINT `FK_CONTIENE2` FOREIGN KEY (`ID_CARRITO`) REFERENCES `carrito_compras` (`ID_CARRITO`);

--
-- Filtros para la tabla `detalle_producto`
--
ALTER TABLE `detalle_producto`
  ADD CONSTRAINT `FK_DETALLE_PRODUCTO` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`),
  ADD CONSTRAINT `FK_DETALLE_PRODUCTO2` FOREIGN KEY (`ID_VENDEDOR`) REFERENCES `vendedor` (`ID_VENDEDOR`);

--
-- Filtros para la tabla `devolucion_de_venta`
--
ALTER TABLE `devolucion_de_venta`
  ADD CONSTRAINT `FK_DEVUELVE` FOREIGN KEY (`ID_USUARIO`) REFERENCES `usuario` (`ID_USUARIO`),
  ADD CONSTRAINT `FK_FACTURA_SE_DEVUELVE2` FOREIGN KEY (`ID_FACTURA`) REFERENCES `factura_de_venta` (`ID_FACTURA`);

--
-- Filtros para la tabla `factura_de_venta`
--
ALTER TABLE `factura_de_venta`
  ADD CONSTRAINT `FK_FACTURA_SE_DEVUELVE` FOREIGN KEY (`ID_DEVOLUCION`) REFERENCES `devolucion_de_venta` (`ID_DEVOLUCION`),
  ADD CONSTRAINT `FK_PAGA_FACTURA` FOREIGN KEY (`ID_PAGO`) REFERENCES `metodo_de_pago` (`ID_PAGO`),
  ADD CONSTRAINT `FK_REALIZA` FOREIGN KEY (`ID_USUARIO`) REFERENCES `usuario` (`ID_USUARIO`),
  ADD CONSTRAINT `FK_TRANSPORTA_FACTURA` FOREIGN KEY (`ID_TRANSPORTADORA`) REFERENCES `transportadora` (`ID_TRANSPORTADORA`);

--
-- Filtros para la tabla `factura_producto`
--
ALTER TABLE `factura_producto`
  ADD CONSTRAINT `FK_FACTURA_PRODUCTO` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`),
  ADD CONSTRAINT `FK_FACTURA_PRODUCTO2` FOREIGN KEY (`ID_FACTURA`) REFERENCES `factura_de_venta` (`ID_FACTURA`);

--
-- Filtros para la tabla `factura_seguimiento`
--
ALTER TABLE `factura_seguimiento`
  ADD CONSTRAINT `FK_FACTURA_SEGUIMIENTO` FOREIGN KEY (`ID_FACTURA`) REFERENCES `factura_de_venta` (`ID_FACTURA`),
  ADD CONSTRAINT `FK_FACTURA_SEGUIMIENTO2` FOREIGN KEY (`ID_SEGUIMIENTO`) REFERENCES `seguimiento` (`ID_SEGUIMIENTO`);

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `FK_PERTENECE_A_UNA_CATEGORIA` FOREIGN KEY (`ID_CATEGORIA`) REFERENCES `categoria` (`ID_CATEGORIA`);

--
-- Filtros para la tabla `producto_devuelve`
--
ALTER TABLE `producto_devuelve`
  ADD CONSTRAINT `FK_PRODUCTO_DEVUELVE` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`),
  ADD CONSTRAINT `FK_PRODUCTO_DEVUELVE2` FOREIGN KEY (`ID_DEVOLUCION`) REFERENCES `devolucion_de_venta` (`ID_DEVOLUCION`);

--
-- Filtros para la tabla `publicidad`
--
ALTER TABLE `publicidad`
  ADD CONSTRAINT `FK_PAGA` FOREIGN KEY (`ID_VENDEDOR`) REFERENCES `vendedor` (`ID_VENDEDOR`);

--
-- Filtros para la tabla `publicidad_producto`
--
ALTER TABLE `publicidad_producto`
  ADD CONSTRAINT `FK_PUBLICIDAD_PRODUCTO` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`),
  ADD CONSTRAINT `FK_PUBLICIDAD_PRODUCTO2` FOREIGN KEY (`ID_PUBLICIDAD`) REFERENCES `publicidad` (`ID_PUBLICIDAD`);

--
-- Filtros para la tabla `resenas`
--
ALTER TABLE `resenas`
  ADD CONSTRAINT `FK_REGISTRA_RESENA` FOREIGN KEY (`ID_USUARIO`) REFERENCES `usuario` (`ID_USUARIO`),
  ADD CONSTRAINT `FK_RESENAS_DEL_PRODUCTO` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`);

--
-- Filtros para la tabla `se_promociona`
--
ALTER TABLE `se_promociona`
  ADD CONSTRAINT `FK_SE_PROMOCIONA` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `producto` (`ID_PRODUCTO`),
  ADD CONSTRAINT `FK_SE_PROMOCIONA2` FOREIGN KEY (`ID_PROMOCION`) REFERENCES `promociones` (`ID_PROMOCION`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `FK_TIENE` FOREIGN KEY (`ID_CARRITO`) REFERENCES `carrito_compras` (`ID_CARRITO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
