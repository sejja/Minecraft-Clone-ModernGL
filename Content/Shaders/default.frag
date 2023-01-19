#version 460 core

in vec2 in_uv;
in vec3 in_normal;
in vec3 in_fragPos;
in vec4 shadowCoord;

out vec4 out_color;

struct Light {
    vec3 position;
};

uniform Light light;
uniform sampler2D u_Texture;
uniform vec3 u_CamPos;
uniform sampler2DShadow u_ShadowMap;
uniform vec2 u_resolution;

float lookup(float ox, float oy) {
    vec2 pixelOffset = 1 / u_resolution;
    return textureProj(u_ShadowMap, shadowCoord + vec4(ox * pixelOffset.x * shadowCoord.w,
                        oy * pixelOffset.y * shadowCoord.w, 0.0, 0.0));
}

float getSoftShadow() {
    float shadow;
    float swidth = 1.0;
    float endp = swidth / 1.5;

    for(float y = -endp; y <= endp; y += swidth) {
        for (float x = -endp; x <= endp; x += swidth) {
            shadow += lookup(x, y);
        }
    }

    return shadow / 16.0;
}

float getShadow() {
    float shadow = textureProj(u_ShadowMap, shadowCoord);
    return shadow;
}

vec3 getLight(vec3 color) {
    vec3 Normal = normalize(in_normal);

    // ambient light
    vec3 ambient = vec3(0.06f, 0.06f, 0.06f);

    // diffuse light
    vec3 lightDir = normalize(light.position - in_fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * vec3(.8f, .8f, .8f);

    // specular light
    vec3 viewDir = normalize(u_CamPos - in_fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * vec3(1.f, 1.f, 1.f);

    float shadow = getSoftShadow();

    return color * (ambient + (diffuse + specular) * shadow);
}


void main() {
    float gamma = 2.2;
    vec3 color = texture(u_Texture, in_uv).rgb;
    color = pow(color, vec3(gamma));

    color = getLight(color);

    color = pow(color, 1 / vec3(gamma));
    out_color = vec4(color, 1.0);
}










