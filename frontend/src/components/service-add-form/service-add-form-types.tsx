import { GetProp, UploadProps } from 'antd';

export interface Rents {
    car_id: number;
    car_license_plate: string;
}

export interface PhotoObj {
    thumbUrl: string;
}

export interface Service {
    id: number;
    name: string;
}

export type FieldType = {
    carLicensePlate: string;
    serviceName: string;
    comment: string;
    images: PhotoObj[];
};

export type FileType = Parameters<GetProp<UploadProps, 'beforeUpload'>>[0];
