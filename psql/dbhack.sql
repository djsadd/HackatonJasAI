PGDMP         -        	        {            hackatosjasai    15.0    15.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    39869    hackatosjasai    DATABASE     �   CREATE DATABASE hackatosjasai WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE hackatosjasai;
                postgres    false            �            1259    40014    person    TABLE     Y   CREATE TABLE public.person (
    id integer NOT NULL,
    title character varying(30)
);
    DROP TABLE public.person;
       public         heap    postgres    false            �            1259    40013    person_id_seq    SEQUENCE     �   CREATE SEQUENCE public.person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.person_id_seq;
       public          postgres    false    215            	           0    0    person_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.person_id_seq OWNED BY public.person.id;
          public          postgres    false    214            �            1259    40021    photo    TABLE     h   CREATE TABLE public.photo (
    id integer NOT NULL,
    encoding_vector text,
    person_id integer
);
    DROP TABLE public.photo;
       public         heap    postgres    false            �            1259    40020    photo_id_seq    SEQUENCE     �   CREATE SEQUENCE public.photo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.photo_id_seq;
       public          postgres    false    217            
           0    0    photo_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.photo_id_seq OWNED BY public.photo.id;
          public          postgres    false    216            j           2604    40017 	   person id    DEFAULT     f   ALTER TABLE ONLY public.person ALTER COLUMN id SET DEFAULT nextval('public.person_id_seq'::regclass);
 8   ALTER TABLE public.person ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            k           2604    40024    photo id    DEFAULT     d   ALTER TABLE ONLY public.photo ALTER COLUMN id SET DEFAULT nextval('public.photo_id_seq'::regclass);
 7   ALTER TABLE public.photo ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217                       0    40014    person 
   TABLE DATA           +   COPY public.person (id, title) FROM stdin;
    public          postgres    false    215   �                 0    40021    photo 
   TABLE DATA           ?   COPY public.photo (id, encoding_vector, person_id) FROM stdin;
    public          postgres    false    217   )                  0    0    person_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.person_id_seq', 14, true);
          public          postgres    false    214                       0    0    photo_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.photo_id_seq', 14, true);
          public          postgres    false    216            m           2606    40019    person person_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.person DROP CONSTRAINT person_pkey;
       public            postgres    false    215            o           2606    40028    photo photo_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.photo
    ADD CONSTRAINT photo_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.photo DROP CONSTRAINT photo_pkey;
       public            postgres    false    217            p           2606    40029    photo photo_person_id_fkey    FK CONSTRAINT     |   ALTER TABLE ONLY public.photo
    ADD CONSTRAINT photo_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(id);
 D   ALTER TABLE ONLY public.photo DROP CONSTRAINT photo_person_id_fkey;
       public          postgres    false    217    3181    215                x   x�˱
�@ �9��|�u��
�AD�\Rj��ER����o�$�e<�Y�H�N�Q#�0G^C�R��a@f��s��S�y'Yj�޳ćn>�~��ЩǤ�$�b���k��OK�2�c��?+]%X            x�M�ٕd�D���h4�����C�|5j-3����$�@  ����O-s�u�l���g��ku��6�]c�{/���Ϯk4�Rg�}|��[ƭu�3nk��b����*��6w[~��L^�e��w�=vۻ����Ų��w��J�</4w�ÇrA�E��yȪ}�{x�u�Rjmk��2N>f��5V��첦/���h>��S��1��=w_mV�=�z��-m>��cǂ�.c��_�爍�:O�u׳���EVW��'�qB�ƫ���~pn��)���~����&������|�[l�6���r❫x8g��z'��i�t�:�����|a/chT�*��G�!k���kˏ�:X(��'��7?}�ٕ`䪁��|����!'����}��*�g��������1.X�\�4�5��'�5}����ZӖ��L̡��م�F�}m�7��p��75�-�.�}b�6��ӿ5.��g�xqX�b�ݮ���o���u�����60.�]9�Uҋ�`��W�#��k�od�|���7�����f�a~�����k�]�淵�.��R͗�Fq\��Ż[�x�v��T����g�k�<���6zqsN�ƒGkk�\���q��Xhu�ұ���4�c���cr\F�ƚ�由�\�����y!�{��/7NGGp��7���b/�g�0�M��܅ۅ˳���ۼ����a���~�b'49�9��4(~��E@�L "^]}��K���(�.�$�z=-�������֌+6wx�8a�:���z���[y2gO$��Y:��_/�xJ��3r�T4w�xa������ƈ��ت�1�-?͇�+^_ ���÷K��#�3��� @�G�Y�Q��`�z�[��7�I��.���`��8�O"��q� x�3�l&���4{����s�	� �`�� X�{,��"�$j������>��d2�*�Y��#��.��5l88FR.͎KDj�i�h!��/��/�0�
�*���	,Tn�GI���ʈ��x�4����w��%8���$z�H$[���W=N���=����S݂� �y^���m�Uva���fYJ�w�7`�O�৑h��v� ?7Q:$�@&fy�?��\���%�M�'>/�oH ǋW��bsC�8џy
��쯋�%�V��g|��[�U&$p2�~k{|<���/9�|
�a������AX�a���8-�gH�B�μ��:W���Xw�0$ب�]a�ľ�õ��#�cE؏78�3��cHdĸ4�T���ڔ��[�d�,�u�=�rX��8�����R�PC��`$��E�S�Hx$���N�yI��t�j���IqC"�% �w[�W����p�y�Ѹ�A��9?�O�?Oi�(H�#6�:9�E���F8Y ��_�1��"Q�4�2ɦs���y6�u	���=(����d^>S��*P�9hM<ڃP/�p)�Ÿ�o�������N���wx��:PE�Ê��r[\kƞ�k�?b�;i�P���U���}n\������E\� c��,�����uH&0���0������E��up�YÔ..����v�pNʞ8Q�<I̎c4'O���%�I,X	�2b���R�m�$���!���ܸ;��E9i����#�-���z~,b8��A7��-9~�L?t������b�-`���S ,�'��%��J��]d+N5�}�
h<沍�HB^��X�3��������h>�8'�Wy
�N�n�ZlZ�O Ix�h2����ҧ��i�f�x�=!x/q�z���j�,� ��A�y��b��ǚ�-�:~��:]����FPVƂ�4>܇�'؏�u-$_mF<��Ih�R<�(�*�\�����r��q� �(W(�*��L*Wh	�kX�ʆZ#��_wڟ��C�-I��҉�Ta����uY:�E�ǫ3G��`Pp܌����LI{�>Jv�c�D2���~Z��șp��Rۑoj�=x���f]Y,d�/��Li
ԧT�qY�� �$d�#�ru�4�AA��,�e�c�˷��<aR�	tm��ed뻴��`���ke���{%8y��8������9��	Ϥ�#�t��*�̚�@|���_���5.���W�F�ް��*5��&��;G�']'�A�yZn,�U�+�Ў�)0-vc�WK��p+8�'�,�!��g���������TV=��|ہ��mFf-T8�)��0�Ix��,��*!:�%��=PP:�O���$I����%4��p�*#S�`�k?��X�p�~����Yq�@�ˈ�W�q���y�:�:م�X��E�H��S�}����o�����<�{�T�-A�7���t����5�N�B���T��<��eW�|ɔ؋X��W�9�*�i�JP��0>���z�Q�'ē(�٣�H~O�>E�jB�YؖO���,�&��EQ�#|�f��	<�1��=��l��w��t}*ن>g㙑5���Cޒ��� j�<r����bb�G]�`;$���,8�uB�z� ğ�<j���ȷds�\���k�Z�鞉���,�4�ԙ%������Byj	F	.`�#G �2��|�8˂Z����[�,"�}&'��L�Lzo*�P�<�{T��bMD&��.�HA�s\�>Ոs#&w�é�$V �)t���S�v#�7�±��
K�9��/$��"pH�*K�.��\wK�����Ij���X��.!���&�>�Kj��Ff����/?S�y����>�8���*66"���{�id.���,�򉻼�
//�0�/5�"_��d-�������Gq��3@N⡇�~kk$���)�?�7/�ӿ)?H�ɓD�j����<�b�@>	NG`sN��y� x�,�Z�0h�����!�2�V��'F�f)�Bl9��'�h���i��X�	
����#��\t�,��ؖ�	{Ae_]x$lR%�nݷ��t�in!h8GX|�l�ΓR���K)[_3���?J����Yԭ�D!��K��]���!P`Wj��ؗT(��*<��"�5�{���A���+��H���@4�i�KI��8�՛��M���|��W
�|�T�wZJJ
��&��I��l�=i�/��6k��zy}�Fm���;�{H�<*��\����j�X
�k��=�[T^���O���>c)RBG���G�h\(]	2���f0�|��>�FyS�R�֧hl�ūT�s�f6��m��8RV�����+6$�'��x�-f���|j?Fj~P]�|���}զ��YZ�İ,��Ȏj��v�C���4�0@:"c�I�8x�Nz��ׅjRæ�<�� ��?���QS�]]�n�_�Sb(�HXY���I�#B����+$;E_8��n��X<�MJâ#���!���N�D�6�|�&M�I"�&��lU�+�|�4�<����v"���X:��m�ĲV*̅��u����dO�q0>-�>���l��=�B�Lܔ�D�g��3�������/k�,����-?�),�e�©���w}�8G[��Y֌��.�1�ʊ�%�a� $�S�t	v���>�Sx�����|�	~��CК��|���8�T�2�RR'F� ��V	��<ŃV�K��a���<�$%>��e��_J�!�r����Z7TJ䞉y.ɺ
�Z���)YA� �J��w�|�W��ێ�-;U��4���O����3p<A_��g���@-�w�ۆ+o*�AlH�!1�M�+"��S���Z�7��v\%[Y������AL��O-?��I"�^�I��/��C�o�a�&ù�T^L��]���8[��)�Jc���Ȝ���C��m?7�^�m�R��(��3JW��NhQ;���`³D��F4%𥚤��o阦{Q�Qq�>�� Sec��*�<g[m���!���O�8�<�ێ&�	��xz���dg�whj@��b��;K��GG�0{RР�`�Cy�RU��$Y���x���eF����3�bZuO�_�a�\�
D�0    }^>���ų�ʞd���m�<x1L&�3e��2h�b�.��hk{�P#���z��JݶK� }��T4�j����]�ڭ��Ӓy8�r0��g�T�;�aH>���l#����f�ၢ�c��y��f�q���U;����݋��c�`���L��cڴ�m��"7�v���C�lj��R~-5º�&¼Ek?V�J���2���ak��E����R�O:�"�ǃ_Dg0B�at~cd	�l��՝O_���1�_&��,�s�9��mx�>�2xk�9����>�5��o��C�6��pA '��{��U�Y�jlI>�h/5�W9��7f���2�l���@��S����cx?��X4a�eWd=q�X	:i��h�ٗ�s�IC�	;!��})�=o������͗���j�C�m�J<
�MruT�3�EcF�J��+*f
i�U��>����	�V��=O�*M�����ۨ��Ft2��#oy�%J��3��wθn%"�H��euj��CJH�[�&���[7�r����ܝl��֐�쮓��J^C��*Qx4d�hX����{%vK��7g�9Ȇ�-�B�v�s06=zI��##[;��&�L�H�?#\��I�����$�6@C���x�U��OIoQHBD���1�*x�w�L{T���lJY2~{gøqy,V���\s^�T�kwwJV�|g�P���(�~=�[{ɲ�oa�Y�D'��R%ܫ����{3�c�){�X̚����<r�Mz�=�+����KV�O��r���c��b#1��Z��:dWɲ�H��Jhp%*{�9�p� DDn{�xZ�����cE~I�	!˔�tU�j_ޚB-C	cc�a�۩�k���PRjS�0����»<	���dw8jr��8A^�����r���1�c}3rӗ�(�L$�;�f�uh�?yS��u������pD"�����vC�l��.iXGr�������6�β���S۟?���0�_������k�&d���$�c6s�N�}�#�z(eT�ay�;o��Qk*za�8��жp��{�B4��POmPv�p�a�Z<T[m��:&	���]�W��:%�C~�Γ��	�Y�^f�����-�V��I��y�]OI񪇀[���땙]��X6�X���m��u�m�G3����٨�(���QLa��U{f_��
�:t�˱���?�j�ō����G�@�VmHZ�բn"P��Ѿ��r8vb1��R�����?�@;��3��U��k�o�4ð�09�ex'��KWh���0][J���`�*K���{��E�2ɦX��Č��� ���ְ�9�V�9����,�9���iu�$�[�!(gˌQˇk�mz�WV���؟�_�(�� ���,�M��8�I�H�li�3q�fb�>�TړCԱ�����Wd8�Fӛ�\6�X��)����U�4�a���T;�=F��m�U�8~ �A��������g*˶�34Rg�����I���h���P���T���>��:7E-�Iثj��xuh��I�YL�7�쇜�L�S|� �P��e8d�[96P,� ���7�ɯ$��ё���(Ψ��?0m���-��"������W=G�4�j�×��~�ͩ���'X��L�*DI,�'�љ`�f��نܱ��eO
.�z���KHa�l�]���u�E���7�lŸ��r2Ir}�'$��9�UhKp<��@R��c]�y��ʠ�b��Q�R�M����`�e�c;���7�!�7c�Fo
R
qD\�8_��˙=M�ت>���&q> ��	�7mCBq�������rVSq��+m����}�RD����:��P	���)[}Zps��ѥ��ܲ�r�Yg��rU˓<��i�&g���ŵ��������=V�Y$�)'���REo��B�83��OI��\	�Q%��Ҳ^���ȣ5�t�g��7ߢ�w�͉�l�5	�tC�_/#c���T��	91�4�V)|*��f�J�yD����q��?.3��_R�p����2܈<]'��9�g�ͺǱ�����������ȂYI-���x�Ik��&�q�������91"p�%V�;�1�X˽&yh��hLN`����b���=љ@@��`&z�����=��)8W ]���Sah�;�f�o����=����FN����2�a�Iݱ?F*��N./�:"8�i竒$^Ip���7j��=/�ت���>�����|�W?L0���&�ٶ�5OTY ����B��~cu�8VĞ;;y=FI$�0�S_��ύ���LS)����SZ�*K�1�T �Nev��)p��=�R�N��a]���Qr�bX�oL.�nP��P��G��������"Z�|��u(�I���;��?ewȕH�3�/��7��arv��?
gwÜ�L�9�d�ދ���`�J��	<�X�UsQ��Ǟ��2M7��v���uف�-'w���j��9v��>p��rNzG�! ��^/�I�BO�r�K�4e�
��OP:�&���];�w,^�b�a��_��X��&+yRT4O�0���R\��VKۖ���5�U���QA���(��Z��	dUㅋ��uz��J��$i��r
8�&+�f������3s�?X�;e�����^s�� �k�l3m|�9�x�s���.�̣^�	��K	C���P?3;�n���m�{��O��N�p�C�oN�z>�cs��q����>+.�97S���p�3:3���1�D�wI�SZ���N,�o�)<g�*S�
߇ٷrL\y��*�Lw�r�'uI��ډΝ��BoV%�1eN[�6��vGq�w/q���e��\I)�k?	N�w��<g�E��d�fS6.�t�~�¾�,r��ʻt������A%Q*o�)f4n�C?���B^ehj9h�g�\�����$^�>� k�Lǩ<��M>��t�ފ�b��}���u�Ǥt���T9V#�^�Jv�����Q�m��x��;r�z:����DkB�M1�
��w���[�~�ʹ.�&�L�P��8�]%�c{ɖ���r��i�a;�q5�7.�R����`��b��_L�G1�|Y���O~)V��	s7��+>c�n��ij�7_Sz$y�'-���9�^�aݰ�Բ�^�0A@,����9���lB���ɋ�c4ͺ�藡-Au��U��Л�:��<�k�gڏ}N�Dί9�m�IF�ӌ�~��n�I��9A�x�;�m	Н�ڶ�� ���ʞ*�{�v��*�-+�"GU��Lʔڂ@׎X�dQ��#&?%c'v"+\���̻֯�B�j���<�m������=�	0���N[���1�؜2�#�'�=�ᗁ��U��<�i�ѯY^!�NO$�p��
q)i����cH&J�gKȵ�.�y��Ӷ���T#R�YO&�9���Wb*�$�`���O���2 arb�@H��h;�<85��w8Dz�'�{�B�Ɖ��
;��Q�Gq��[�[x�m�|nE;�n��1�[�Ӣj�$����<��[���l%��y�������ѷ���r$��z����YF/���c�7��Mb�e;f�ͨ;?�X�k�]�鬂X{�^����B�5�y���a��!��jb�5��$��#��o����HJ��|���yEOQ��6e����R���m�wg�!0���n����y����W�;D�A�$�9�R�=o�h\bJ���E�����`�޸#]C
���e�X.���k/z�mv����K�>L�K�,�͹ݘ���هU������\��dŎϼ�:��Y�2*�@��gE3"�R5�Βt���1�;G�r՛���&Y����q�̯�t4�5[_y�܁q�3��C6���|8ku�K��{m�����~LM{�EZ���o���kE-.��L2]�e�-K�Ͷ]|Ur�i��.�^95���Ṟ>h�%���w9����[�^����|T�+�*O���U���$���H\װ�������>�4�#��d�+%�8��6�t�UIPy���t,��N�%�7H�i�s�˽�~�=A��&�����ұ�w�g��f��#�k2ODl# c  �����Ɠ"�w���7���	��8���#��x3�˨� ��bLy�+��8�f�&oF��~C\�� �^����N�E㓿�;o壆-m�A�l�{m .�9��@lց#�Ps��g�rU��dR%se}/�\���i��ðo�ס�I�sqx`���!lzѲ|r��A�-Y������d���wO��e�b���ˆ����*y�w��q+�|�<U�DX�|��+���/��pX��!H������)>c�8����ǁY��wY��D�J�O'�t��>G��L6^���}[x��W����qnۨ+
#ozQh/o[ɿaܽ!�k����%^\�������U��n��q���J�ɛR�]R���`��W��~�S��{V�a���Þ�d�)�^�p�N�ߟ��E��� �72����9C��P��Cm�lWp�n���IY����uE��UOzJh�;�{�C�g�t�@��e�O������ӄHoB�܌$�~g��^Kr
?�P1�c���ڳ�f;���,���F�7b��.��� �3�;=6���������v/vڅ{m,g6��1�ڿd���wJB��,�/9>�򧎟������?�fC�     