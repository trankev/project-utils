rule "terraform_naming_convention" {
    enabled = true
    format = "snake_case"
}

rule "terraform_deprecated_index" {
    enabled = true
}

rule "terraform_comment_syntax" {
    enabled = true
}

rule "terraform_documented_variables" {
    enabled = true
}

rule "terraform_typed_variables" {
    enabled = true
}

rule "terraform_unused_required_providers" {
    enabled = true
}
