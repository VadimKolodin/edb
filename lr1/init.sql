create schema clinic;

create table clinic.drugs
(
    id          uuid
        primary key,
    name        varchar not null
        unique,
    description varchar
);

create table clinic.patients
(
    id        uuid
        primary key,
    fio       varchar not null,
    birthdate date    not null,
    gender    boolean not null,
    ethnicity varchar,
    education int
);
create table clinic.patients_personalities
(
    patient_id uuid
        primary key
        constraint patients_personalities_patients_id_fk
            references clinic.patients (id),
    n_score    real not null,
    e_score    real not null,
    o_score    real not null,
    c_score    real not null,
    impulsive  real not null,
    sensation  real not null
);
create type clinic.consumption as enum ('CL0', 'CL1', 'CL2', 'CL3', 'CL4', 'CL5', 'CL6');
create table clinic.patients_consumption
(
    patient_id uuid
        constraint patients_consumption_patients_id_fk
            references clinic.patients (id),
    drug_id    uuid
        constraint patients_consumption_drugs_id_fk
            references clinic.drugs (id),
    usage      clinic.consumption not null,
    constraint patients_consumption_pk
        primary key (patient_id, drug_id)
);

create table clinic.doctors
(
    id        uuid
        primary key,
    fio       varchar not null,
    birthdate date    not null,
    gender    boolean not null,
    room      int
);

    create table clinic.patients_doctors_appointments
(
    id                   uuid primary key,
    patient_id           uuid
        constraint patients_appointments_patients_id_fk
            references clinic.patients (id),
    doctor_id            uuid
        constraint patients_appointments_doctors_id_fk
            references clinic.doctors (id),
    appointment_datetime timestamp not null,
    is_committed boolean not null default false
);

create index patients_id_index
    on clinic.patients (id);

create index doctors_id_index
    on clinic.doctors (id);

create index drugs_id_index
    on clinic.drugs (id);

create index appointments_id_index
    on clinic.patients_doctors_appointments (id);
