import {
    RouterProvider,
    createBrowserRouter,
    createRoutesFromElements,
    Route,
    Navigate,
} from 'react-router-dom';
import { ProtectedRoute } from '../routes/projected-route';

import 'antd/dist/reset.css';
import App from '../App';
import ErrorPage from '../error-page';
import ListOfCars from '../pages/cars-page/cars-page';
import { CarAPI } from '../api/cars-api';
import { CarPage } from '../pages/car-page/car-page';
import NotFoundPage from '../not-found';
import { LoginPage } from '../pages/login-page/login-page';
import { Logout } from '../pages/logout-page/logout-page';
import { RegisterPage } from '../pages/register-page/register-page';
import { TestPage } from '../pages/test_page/test-page';
import { UserPage } from '../pages/user-page/user-page';
import { AddServiceForm } from '../components/service-add-form/service-add-form';
import { EditServiceForm } from '../components/service-edit-form/service-edit-form';

export const Routes = () => {
    const router = createBrowserRouter(
        createRoutesFromElements(
            <Route path="/" element={<App />} errorElement={<ErrorPage />}>
                <Route errorElement={<ErrorPage />}>
                    <Route index path="cars/" element={<ListOfCars />} />
                    <Route
                        path="cars/:carId"
                        element={<CarPage />}
                        loader={CarAPI.carLoader}
                    />
                    <Route path="login" element={<LoginPage />} />
                    <Route path="logout" element={<Logout />} />
                    <Route path="register" element={<RegisterPage />} />
                    {/* <Route path="1" element={<TestPage />} /> */}
                    <Route path="/" element={<ProtectedRoute />}>
                        <Route
                            path="services/:serviceId/edit/"
                            element={<EditServiceForm />}
                        />
                        <Route path="user" element={<UserPage />} />
                        <Route
                            path="/"
                            element={<Navigate to="cars/" replace />}
                        />
                        <Route
                            path="services/add/"
                            element={<AddServiceForm />}
                        />
                    </Route>
                    <Route path="/" element={<Navigate to="cars/" replace />} />
                    <Route path="*" element={<NotFoundPage />} />
                    // TODO проверка маршрутов
                </Route>
            </Route>
        )
    );

    return <RouterProvider router={router} />;
};
