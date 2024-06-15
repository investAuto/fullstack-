import React, { useState, useEffect } from 'react';
import { Layout } from 'antd';
import { UserOutlined } from '@ant-design/icons';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../context/auth-provider';

const { Header, Content, Footer } = Layout;

const headerStyle: React.CSSProperties = {
    display: 'flex',
    justifyContent: 'space-between',
    textAlign: 'center',
    color: '#fff',
    height: 64,
    paddingInline: 48,
    lineHeight: '64px',
    backgroundColor: '#ff7a45',
};

const contentStyle: React.CSSProperties = {
    padding: '10px',
    textAlign: 'center',
    minHeight: 'calc(100vh - 128px)',
    color: '#fff',
    backgroundColor: '#fff2e8',
};

const footerStyle: React.CSSProperties = {
    textAlign: 'center',
    color: '#fff',
    backgroundColor: '#ff7a45',
};

const layoutStyle = {
    borderRadius: 8,
    overflow: 'hidden',
    width: '100%',
    maxWidth: '100%',
};

const loginButtonStyle = {
    textShadow: 'white 2px 0 10px',
};

type Props = {
    children?: React.ReactNode;
};

const Template: React.FC<Props> = ({ children }) => {
    const { token } = useAuth();
    const [phoneNumber, setPhoneNumber] = useState(
        localStorage.getItem('phone')
    );

    useEffect(() => {
        const initialPhone = localStorage.getItem('phone');

        setPhoneNumber(initialPhone);

        // Слушаем событие на изменение localStorage
        const handleStorageChange = (e: StorageEvent) => {
            if (e.key === 'phone') {
                setPhoneNumber(e.newValue || '');
            }
        };

        // Добавляем и удаляем слушатель событий при монтировании и демонтировании
        window.addEventListener('storage', handleStorageChange);
        return () => window.removeEventListener('storage', handleStorageChange);
    }, [token]);

    return (
        <Layout style={layoutStyle}>
            <Header style={headerStyle}>
                <NavLink to={'/1'} style={loginButtonStyle}>
                    <div>Тестовая</div>
                </NavLink>
                <NavLink to={'/'} style={loginButtonStyle}>
                    <div>Header</div>
                </NavLink>

                <NavLink to={'register'} style={loginButtonStyle}>
                    регистрация
                </NavLink>
                {phoneNumber ? (
                    <NavLink to={'/user/'} style={loginButtonStyle}>
                        {phoneNumber}
                    </NavLink>
                ) : (
                    <NavLink to={'login'} style={loginButtonStyle}>
                        <UserOutlined />
                        Войти
                    </NavLink>
                )}
                <NavLink to={'/logout'} style={loginButtonStyle}>
                    <UserOutlined /> Выйти
                </NavLink>
            </Header>
            <Content style={contentStyle}>{children}</Content>
            <Footer style={footerStyle}>Footer</Footer>
        </Layout>
    );
};

export default Template;