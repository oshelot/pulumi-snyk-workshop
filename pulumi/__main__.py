import pulumi
import pulumi_aws as aws

# Config and secrets (ESC preferred; fallback to per-stack secret)
cfg = pulumi.Config()
# Expect a secret set via ESC or: pulumi config set --secret db.password "S3cret!"
db_password = cfg.get_secret("db.password")

# INTENTIONALLY INSECURE START (for Challenge 3)
bucket = aws.s3.Bucket(
    "workshop-bucket",
    acl="public-read",  # insecure default to trigger policy
    # server_side_encryption_configuration is missing initially
    tags={
        # 'env' tag intentionally missing to trigger policy
        "owner": "workshop"
    },
)

# Learners fix to something like:
# bucket = aws.s3.Bucket(
#     "workshop-bucket",
#     acl="private",
#     server_side_encryption_configuration=aws.s3.BucketServerSideEncryptionConfigurationArgs(
#         rules=[aws.s3.BucketServerSideEncryptionConfigurationRuleArgs(
#             apply_server_side_encryption_by_default=aws.s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
#                 sse_algorithm="AES256"
#             )
#         )]
#     ),
#     tags={
#         "owner": "workshop",
#         "env": "dev"
#     },
# )

# Prove secret presence without printing it
secret_present = db_password.apply(lambda _: True) if db_password else False

pulumi.export("bucketName", bucket.id)
pulumi.export("dbPasswordSet", secret_present)
