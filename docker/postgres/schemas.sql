CREATE TABLE leads (
    lead_uuid UUID NOT NULL PRIMARY KEY,
    requested DECIMAL(18, 9),
    loan_purpose VARCHAR(500),
    credit VARCHAR(20),
    annual_income DECIMAL(18, 9)
);

CREATE TABLE offers (
    lead_uuid UUID NOT NULL,
    offer_id INT NOT NULL PRIMARY KEY,
    apr DECIMAL(18, 9),
    lender_id INT NOT NULL,
    FOREIGN KEY(lead_uuid) REFERENCES leads(lead_uuid)
);

CREATE TABLE clicks (
    offer_id INT NOT NULL PRIMARY KEY,
    clicked_at TIMESTAMP NOT NULL,
--     INDEX click_dt(clicked_at),
    CONSTRAINT fk_offer_id FOREIGN KEY(offer_id) REFERENCES offers(offer_id)
);

CREATE TABLE model_artifacts (
    model_uuid UUID NOT NULL PRIMARY KEY,
    pickled_model BYTEA NOT NULL,
    description VARCHAR(500)
);