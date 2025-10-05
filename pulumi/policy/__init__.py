from pulumi_policy import PolicyPack, ReportViolation
from typing import Any, Dict

# Simple type check helper
def is_s3_bucket(args: Dict[str, Any]) -> bool:
    return args.get("type") == "aws:s3/bucket:Bucket"

def get_tags(props: Dict[str, Any]) -> Dict[str, str]:
    return (props or {}).get("tags") or {}

def has_sse(props: Dict[str, Any]) -> bool:
    # Pulumi AWS classic sets this prop when configured
    return bool(props.get("serverSideEncryptionConfiguration"))

def is_public_acl(props: Dict[str, Any]) -> bool:
    return props.get("acl") in {"public-read", "public-read-write"}

def s3_encryption_required(args, report: ReportViolation):
    if is_s3_bucket(args):
        props = args.get("props", {})
        if not has_sse(props):
            report("S3 bucket missing server-side encryption.")

def s3_no_public_acl(args, report: ReportViolation):
    if is_s3_bucket(args):
        props = args.get("props", {})
        if is_public_acl(props):
            report("S3 bucket ACL must not be public.")

def tag_env_required(args, report: ReportViolation):
    if is_s3_bucket(args):
        tags = get_tags(args.get("props", {}))
        if "env" not in tags:
            report("Resources must include an 'env' tag.")

PolicyPack(
    name="security-baseline",
    policies=[
        {
            "name": "s3-encryption-required",
            "description": "S3 buckets must have SSE enabled.",
            "enforcementLevel": "mandatory",
            "validateResource": s3_encryption_required,
        },
        {
            "name": "s3-no-public-acl",
            "description": "S3 buckets must not be publicly readable.",
            "enforcementLevel": "mandatory",
            "validateResource": s3_no_public_acl,
        },
        {
            "name": "tag-env-required",
            "description": "All buckets must include env tag.",
            "enforcementLevel": "mandatory",
            "validateResource": tag_env_required,
        },
    ],
)
