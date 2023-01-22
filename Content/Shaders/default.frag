#version 460 core

layout (location = 0) out vec4 fragColor;

in vec2 in_UV;
in vec3 in_Normal;
in vec3 in_Pos;
in vec4 in_Shadowcord;

struct Light {
    vec3 position;
};

uniform Light u_light;
uniform sampler2D u_texture;
uniform vec3 u_CamPos;
uniform sampler2DShadow u_shadowmap;
uniform vec2 u_resolution;

float lookup(float ox, float oy) {
    vec2 pixelOffset = 1 / u_resolution;
    return textureProj(u_shadowmap, in_Shadowcord + vec4(ox * pixelOffset.x * in_Shadowcord.w,
                        oy * pixelOffset.y * in_Shadowcord.w, 0.0, 0.0));
}

float getShadow() {
    float shadow;

    for(int y = -1; y <= 1; y++) {
        for (int x = -1; x <= 1; x++) {
            shadow += lookup(x, y);
        }
    }

    return shadow / 16.0;
}

vec3 getLight(vec3 color) {
    vec3 Normal = normalize(in_Normal);
    vec3 lightDir = normalize(u_light.position - in_Pos);
    return color * (vec3(0.05, 0.05f, 0.05f) + (max(0, dot(lightDir, Normal)) * vec3(.8f, .8f, .8f) + vec3(pow(max(dot(normalize(u_CamPos - in_Pos), reflect(-lightDir, Normal)), 0), 32))) * getShadow());
}


void main() {
    fragColor = vec4(pow(getLight(pow(texture(u_texture, in_UV).rgb, vec3(5))), 1 / vec3(5)), 1.0);
}
