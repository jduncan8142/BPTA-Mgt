"""Create user model

Revision ID: 4df8c5a5c94f
Revises: 82a2ed8f1d6a
Create Date: 2023-03-06 22:55:44.009995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4df8c5a5c94f'
down_revision = '82a2ed8f1d6a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('finish_date', sa.Date(), nullable=True),
    sa.Column('project_manager', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['project_manager'], ['user.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('case',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('process_owner_id', sa.Integer(), nullable=False),
    sa.Column('it_owner_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('doc_link', sa.String(length=1024), nullable=False),
    sa.Column('date_format', sa.String(length=10), nullable=False),
    sa.Column('explicit_wait', sa.Float(), nullable=False),
    sa.Column('screenshot_on_pass', sa.Boolean(), nullable=False),
    sa.Column('screenshot_on_fail', sa.Boolean(), nullable=False),
    sa.Column('fail_on_error', sa.Boolean(), nullable=False),
    sa.Column('exit_on_fail', sa.Boolean(), nullable=False),
    sa.Column('system', sa.String(length=256), nullable=False),
    sa.Column('system_metadata', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['it_owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['process_owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.PickleType(), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('step',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=96), nullable=False),
    sa.Column('element_id', sa.String(length=1024), nullable=True),
    sa.Column('args', sa.ARRAY(sa.String(length=256)), nullable=True),
    sa.Column('kwargs', sa.JSON(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('system_metadata', sa.JSON(), nullable=True),
    sa.Column('py_code', sa.String(length=2048), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=True),
    sa.Column('step_id', sa.Integer(), nullable=True),
    sa.Column('test_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('result_type', sa.Enum(), nullable=False),
    sa.Column('result', sa.Enum(), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['step_id'], ['step.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('updated', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated')
    op.drop_table('result')
    op.drop_table('step')
    op.drop_table('data')
    op.drop_table('case')
    op.drop_table('project')
    # ### end Alembic commands ###
