--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Debian 14.2-1+b3)
-- Dumped by pg_dump version 14.2 (Debian 14.2-1+b3)

-- Started on 2022-07-23 16:49:48 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16386)
-- Name: passwords; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.passwords (
    id bigint DEFAULT nextval('public.id_inc'::regclass) NOT NULL,
    password character varying(255),
    username character varying(255),
    url character varying(255)
);


ALTER TABLE public.passwords OWNER TO postgres;

--
-- TOC entry 3323 (class 0 OID 16386)
-- Dependencies: 209
-- Data for Name: passwords; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.passwords (id, password, username, url) FROM stdin;
1	alpha456	alpha123	facebook.com
2	beta456	beta123	twitter.com
3	gamma456	gamma123	
4	dbsmmJvZCDqQyV8cXfEP	dominico@gmail.com	linkedin.com
\.


--
-- TOC entry 3183 (class 2606 OID 16394)
-- Name: passwords passwords_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.passwords
    ADD CONSTRAINT passwords_pkey PRIMARY KEY (id);


-- Completed on 2022-07-23 16:49:49 EDT

--
-- PostgreSQL database dump complete
--

