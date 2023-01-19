#version 460 core

in vec4 clipCoords;
out vec4 out_Color;

uniform samplerCube u_Texture;
uniform mat4 u_mProj;

void main() {
    vec4 worldCoords = u_mProj * clipCoords;
    out_Color = texture(u_Texture, normalize(worldCoords.xyz / worldCoords.w));
}