#version 460 core

layout (location = 0) in vec2 in_texcoord_0;
layout (location = 1) in vec3 in_normal;
layout (location = 2) in vec3 in_position;

out vec2 in_UV;
out vec3 in_Normal;
out vec3 in_Pos;
out vec4 in_Shadowcord;

uniform mat4 m_Proj;
uniform mat4 m_View;
uniform mat4 m_ViewLight;
uniform mat4 m_Model;

mat4 m_shadow_bias = mat4(
    0.5, 0.0, 0.0, 0.0,
    0.0, 0.5, 0.0, 0.0,
    0.0, 0.0, 0.5, 0.0,
    0.5, 0.5, 0.5, 1.0);

void main() {
    in_Shadowcord =  m_shadow_bias * m_Proj * m_ViewLight * m_Model * vec4(in_position, 1.0);
    in_Shadowcord.z -= 0.0001;
    in_UV = in_texcoord_0;
    in_Pos = vec3(m_Model * vec4(in_position, 1.0));
    in_Normal = mat3(transpose(inverse(m_Model))) * normalize(in_normal);
    gl_Position = m_Proj * m_View * m_Model * vec4(in_position, 1.0);
}