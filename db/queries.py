get_leads_query: str = """
SELECT * FROM leads;
"""

get_offers_query: str = """
SELECT * FROM offers;
"""

get_clicks_query: str = """
SELECT * FROM clicks;
"""

truncation_query: str = """
TRUNCATE TABLE clicks CASCADE;
TRUNCATE TABLE offers CASCADE;
TRUNCATE TABLE leads CASCADE;
"""

write_model_artifact_query: str = """
INSERT INTO model_artifacts VALUES ('{model_uuid}', {pickled_model}, '{description}');
"""

read_model_artifact_query: str = """
SELECT * FROM model_artifacts WHERE model_uuid='{model_uuid}';
"""

get_all_models_query: str = """
SELECT model_uuid, description, created_at FROM model_artifacts;
"""
